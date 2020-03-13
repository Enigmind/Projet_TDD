'''Model :
This file lists all the tables in the database
Each class is a table and each variable is a field
 '''
from django.db import models

EXPORT_CONTROL = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]


class ProductLine(models.Model):
    """Table Productline (a productline own many systemnames)

    :param models: Inherited from model
    :type models: django.db.models
    :return: Name of the product line
    :rtype: CharField
    """

    name = models.CharField(max_length=50, unique=True)

    # display 'name' instead of primary key when we call for this model
    def __str__(self):
        return self.name


class SystemName(models.Model):
    """Table SystemName

    :param models: Inherited from model
    :type models: django.db.models
    :return: Name of the System Name
    :rtype: CharField
    """

    # fields
    name = models.CharField(max_length=50, unique=True)

    # display 'name' instead of primary key when we call for this model
    def __str__(self):
        return self.name


class Airframer(models.Model):
    """Table Airframer (an airframer own many aircrafts)

    :param models: Inherited from model
    :type models: django.db.models
    :return: Name of the Airframer
    :rtype: CharField
    """

    name = models.CharField(max_length=30, unique=True)

    # display 'name' instead of primary key when we call for this model
    def __str__(self):
        return self.name


class Aircraft(models.Model):
    """Table Aircraft (an aircraft belongs to an airframer)

    :param models: Inherited from model
    :type models: django.db.models
    :return: Name of the Aircraft
    :rtype: CharField
    """

    # Foreign Keys
    airframer = models.ForeignKey(
        Airframer, default='', on_delete=models.CASCADE)

    # Block Product Data
    name = models.CharField(max_length=30, unique=True)
    # remark in tab product data
    PD_remarks = models.TextField(null=True, blank=True, max_length=200)

    # Block Airframer Data
    ramp_up_by_year = models.CharField(null=True, blank=True, max_length=200)
    fh_year = models.PositiveIntegerField(
        null=True, blank=True)  # Number of flight hours by year

    # number of flight hours by day
    daily_fh = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=3)

    fc_year = models.PositiveIntegerField(null=True, blank=True)
    warranty_duration_new_product = models.PositiveSmallIntegerField(
        null=True, blank=True)

    warranty_duration_repaired_product = models.PositiveSmallIntegerField(
        null=True, blank=True)

    # remark in tab airframer data
    AD_remarks = models.TextField(null=True, blank=True, max_length=200)

    # display 'name' instead of primary key when we call for this model
    def __str__(self):
        return self.name


class LruDenomination(models.Model):
    """Table LRU Denomination (the LRU denomination is the name of the LRU.
    It declines in many PN defined in the table LRU)
    A LRU can be belongs to many aircraft (n-n relation)

    :param models: Inherited from model
    :type models: django.db.models
    :return: Name of the LRU Denomination
    :rtype: CharField
    """

    name = models.CharField(max_length=50, unique=True)

    # display 'name' instead of primary key when we call for this model
    def __str__(self):
        return self.name


class SruDenomination(models.Model):
    """Table SRU Denomination (the SRU denomination is the name of the SRU.
    It declines in many PN defined in the table SRU)
    A SRU can belongs to many LRU (n-n relation)

    :param models: Inherited from model
    :type models: django.db.models
    :return: Name of the SRU Denomination
    :rtype: CharField
    """

    name = models.CharField(max_length=50, unique=True)

    # display 'name' instead of primary key when we call for this model
    def __str__(self):
        return self.name


class LRU(models.Model):
    """Table LRU (a LRU can be spotted in many aircraft and own many SRU (n-n relation))
    It belongs to a systemname is a declination of a LRU denomination

    :param models: Inherited from model
    :type models: django.db.models
    :return: PN of the LRU
    :rtype: CharField
    """

    # choice type for LRU
    TYPE = [
        ('SFE', 'SFE'),
        ('BFE', 'BFE'),
        ('SSFE', 'SSFE'),
        ('Option', 'Option'),
        ('SFE/BFE', 'SFE/BFE'),
    ]

    # Foreign Keys
    product_line = models.ForeignKey(
        ProductLine, default='', on_delete=models.CASCADE)

    system_name = models.ForeignKey(
        SystemName, default='', on_delete=models.CASCADE)

    aircraft = models.ForeignKey(
        Aircraft, default='', on_delete=models.CASCADE)

    lru_denomination = models.ForeignKey(
        LruDenomination, default='', on_delete=models.CASCADE)

    ### Block product basic data ###

    # declination of LRU denomination
    pn = models.CharField(max_length=30, unique=True)

    repair_lvl = models.PositiveSmallIntegerField(null=True, blank=True)
    supplier = models.CharField(null=True, blank=True, max_length=30)
    type_lru = models.CharField(
        choices=TYPE, null=True, blank=True, max_length=10)

    ramp_up_year = models.CharField(null=True, blank=True, max_length=200)
    export_control = models.CharField(
        choices=EXPORT_CONTROL, null=True, blank=True, max_length=5)

    PBD_remarks = models.TextField(null=True, blank=True, max_length=200)

    # Block estimated perfo
    mtbf = models.PositiveIntegerField(null=True, blank=True)
    mtbur = models.PositiveIntegerField(null=True, blank=True)
    nff_rate = models.PositiveIntegerField(
        null=True, blank=True)

    tte1 = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=3)
    EP_remarks = models.TextField(null=True, blank=True, max_length=200)

    # Block commitments
    g_mtbur = models.PositiveIntegerField(null=True, blank=True)
    specified_mtbf = models.PositiveIntegerField(null=True, blank=True)
    g_mtbf = models.PositiveIntegerField(null=True, blank=True)
    specified_nff = models.PositiveIntegerField(null=True, blank=True)
    g_dmc_unit = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=3)

    g_dmc_ac = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=3)

    spare_price = models.PositiveIntegerField(null=True, blank=True)
    warranty_duration_new_product = models.PositiveSmallIntegerField(
        null=True, blank=True)

    warranty_duration_repaired_product = models.PositiveSmallIntegerField(
        null=True, blank=True)

    specified_mtte1 = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=3)

    C_remarks = models.TextField(null=True, blank=True, max_length=200)

    # Block economic data
    cpp_cci = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=3)
    cpp_asw = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=3)
    cpp_repair = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=3)
    cpp_nff = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=3)
    cost_dmc_unit = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=3)
    cost_dmc_ac = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=3)
    ED_remarks = models.TextField(null=True, blank=True, max_length=200)

    # display 'pn' instead of primary key when we call for this model
    def __str__(self):
        return self.pn


class SRU(models.Model):
    """Table SRU (a SRU can be spotted in many LRU)
    It belongs to a LRU is a declination of a SRU denomination

    :param models: Inherited from model
    :type models: django.db.models
    :return: PN of the SRU
    :rtype: CharField
    """

    # Foreign Keys
    sru_denomination = models.ForeignKey(
        SruDenomination, default='', on_delete=models.CASCADE)

    lru = models.ForeignKey(
        LRU, default='', on_delete=models.CASCADE)

    # Block Product basic data
    pn = models.CharField(max_length=30, unique=True)
    repair_lvl = models.SmallIntegerField(null=True, blank=True)
    supplier = models.CharField(null=True, blank=True, max_length=50)
    export_control = models.CharField(
        choices=EXPORT_CONTROL, null=True, blank=True, max_length=5)

    PBD_remarks = models.TextField(null=True, blank=True, max_length=200)

    # Block Estimated perfo
    mtbf = models.IntegerField(null=True, blank=True)
    EP_remarks = models.TextField(null=True, blank=True, max_length=200)

    # Block Commitments
    warranty_duration_new_product = models.SmallIntegerField(
        null=True, blank=True)

    warranty_duration_repaired_product = models.SmallIntegerField(
        null=True, blank=True)

    C_remarks = models.TextField(null=True, blank=True, max_length=200)

    # Block economic data
    cpp_cci = models.CharField(null=True, blank=True, max_length=100)
    cpp_asw = models.CharField(null=True, blank=True, max_length=100)
    cpp_repair = models.CharField(null=True, blank=True, max_length=100)
    ED_remarks = models.TextField(null=True, blank=True, max_length=200)

    # display 'pn' instead of primary key when we call for this model
    def __str__(self):
        return self.pn

from rest_framework import serializers
from APILS.models import *

class AircraftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft
        fields = ('name', 'fh_year', 'daily_fh', 'warranty_duration_repaired_product')
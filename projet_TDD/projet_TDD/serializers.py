from rest_framework import serializers
from django.contrib.auth.models import User
from APILS.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class AircraftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft
        fields = ('name', 'fh_year', 'daily_fh', 'warranty_duration_repaired_product')
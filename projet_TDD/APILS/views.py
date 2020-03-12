from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.shortcuts import render
from rest_framework import viewsets
from APILS.models import *
from projet_TDD.serializers import *
from django.contrib.auth.models import User
from projet_TDD.serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
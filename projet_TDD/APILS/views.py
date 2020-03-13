from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django.shortcuts import render
from rest_framework import viewsets
from APILS.models import *
from projet_TDD.serializers import *
from django.contrib.auth.models import User
from projet_TDD.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import simplejson as json  


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def get_aircraft(request):
    """API endpoint that return datas viewed in he dashboard
    according to parameters in POST request

    Arguments:
        request {[type]} -- [description]

    Returns:
        [HttpResponse] -- [JSON]
    """

    try:
        current = {}
        aircraft = Aircraft.objects.get(name=request.data['aircraft']) 

        current = {
            'aircraft': aircraft.name,
            'flight_hours_per_year': aircraft.fh_year,
            'Warrranty_duration': aircraft.warranty_duration_new_product,
            
        }

        return HttpResponse(json.dumps(current), status=200)
    except Exception as identifier:
        print("A problem occured :"+str(identifier))
        return HttpResponseNotFound('<h1>FATAL ERROR </h1>\n' + str(identifier))
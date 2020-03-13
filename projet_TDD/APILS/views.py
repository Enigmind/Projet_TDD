import simplejson as json  
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from APILS.models import *
from projet_TDD.serializers import UserSerializer

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
def get_airframer(request):

    current = {}
    try:
        airframer = Airframer.objects.get(name=request.data['airframer']) 

        current = {
            'airframer': airframer.name,
        }

        return HttpResponse(json.dumps(current), status=200)
    except Exception as identifier:
        print("A problem occured :"+str(identifier))
        return HttpResponseNotFound('<h1>FATAL ERROR </h1>\n' + str(identifier))

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def get_aircraft(request):

    current = {}
    try:
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

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def count_aircrafts(request):

    current = {}
    try:
        count = Aircraft.objects.all().count()
        current = {
            'count_aircrafts': count,
        }

        return HttpResponse(json.dumps(current), status=200)
    except Exception as identifier:
        print("A problem occured :"+str(identifier))
        return HttpResponseNotFound('<h1>FATAL ERROR </h1>\n' + str(identifier))
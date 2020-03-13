from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from APILS.models import *



# Create your tests here.
class ListAPIViewTestCase(APITestCase):

    def setUp(self):
        # create test user
        self.user = User.objects.create_user(
            username="testuser",
            email="user1@test.com",
            password="password1",
            is_staff=True)

        self.client = APIClient()

        # create fake models
        test_airframer = Airframer.objects.create(name='test_airframer')
        test_airframer.save()
        test_aircraft = Aircraft.objects.create(
            airframer=Airframer.objects.get(
                name=test_airframer.name), 
                name='test_aircraft')
        test_aircraft.save()

        test_productline = ProductLine.objects.create(name='test_productline')
        test_productline.save()

        test_systemname = SystemName.objects.create(name='test_systemname')
        test_systemname.save()

        test_lru_denom = LruDenomination.objects.create(name='test_lru_denom')
        test_lru_denom.save()

        test_sru_denom = SruDenomination.objects.create(name='test_sru_denom')
        test_sru_denom.save()

        test_lru = LRU.objects.create(
            product_line=ProductLine.objects.get(name=test_productline.name),
            system_name=SystemName.objects.get(name=test_systemname.name),
            aircraft=Aircraft.objects.get(name=test_aircraft.name),
            lru_denomination=LruDenomination.objects.get(
                name=test_lru_denom.name),
            pn='test_lru')
        test_lru.save()

        test_sru = SRU.objects.create(
            sru_denomination=SruDenomination.objects.get(
                name=test_sru_denom.name),
            lru=LRU.objects.get(pn=test_lru.pn),
            pn='test_sru')
        test_sru.save()

    def test_access_api_without_credentials(self):
        # creation of the request
        response = self.client.get('http://localhost:8000/users/')

        # response verification
        self.assertEqual(
            response.data, {"detail": "Authentication credentials were not provided."})

    def test_get_aircraft_from_api(self):
        # authentication
        # Include an appropriate `Authorization:` header on all requests.
        client = APIClient()

        # creation of the request
        response = client.post(
            'http://localhost:8000/getAircraft/',
            {
                'aircraft': 'test_aircraft'
            },
            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

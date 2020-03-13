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
        response = self.client.get('/users/')

        # response verification
        self.assertEqual(
            response.data, {"detail": "Authentication credentials were not provided."})

    def test_get_airframer_from_api(self):

        client = APIClient()

        # creation of the request
        response = client.post(
            '/getAirframer/',
            {
                'airframer': 'test_airframer'
            },
            format='json')

        # response verification
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_aircraft_from_api(self):
        client = APIClient()

        # creation of the request
        response = client.post(
            '/getAircraft/',
            {
                'aircraft': 'test_aircraft'
            },
            format='json')

        # response verification
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_count_aircrafts_view_access(self):
        client = APIClient()

        # creation of the request
        response = client.post(
            '/countAircrafts/',
            {
                'element': 'count'
            },
            format='json')

        # response verification
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_count_aircrafts_view(self):
        #there is already an aircraft in test database, we create 3 more aircrafts
        ac2 = Aircraft.objects.create(
            airframer=Airframer.objects.get(
                name="test_airframer"),
            name='ac2')
        ac3 = Aircraft.objects.create(
            airframer=Airframer.objects.get(
                name="test_airframer"),
            name='ac3')
        ac4 = Aircraft.objects.create(
            airframer=Airframer.objects.get(
                name="test_airframer"),
            name='ac4')
        ac2.save()
        ac3.save()
        ac4.save()

        client = APIClient()

        # creation of the request
        response = client.post(
            '/countAircrafts/',
            {
                'element': 'count'
            },
            format='json')

        # response verification
        self.assertEqual(response.content, b'{\"count_aircrafts\": 4}')

    def test_add_aiframer_in_db_via_api(self):

        client = APIClient()

        # creation of the request
        client.post(
            '/addElement/',
            {
                'element': 'airframer',
                'name': 'new_airframer',
            },
            format='json')

        exists = Airframer.objects.filter(name="new_airframer").exists()

        # response verification
        self.assertEqual(exists, True)

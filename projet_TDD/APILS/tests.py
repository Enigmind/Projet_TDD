from django.contrib.auth.models import User
from django.test import TestCase
from APILS.models import *
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate, APIClient

# Create your tests here.
class ListAPIViewTestCase(APITestCase):

    def setUp(self):
        #create test user
        test_user = User.objects.create_user('testuser', 'testemail@test.com', 'P@ssw0rd')
        test_user.save()

        #create fake models
        test_airframer = Airframer.objects.create(name='test_airframer')
        test_airframer.save()
        test_aircraft = Aircraft.objects.create(airframer=Airframer.objects.get(name=test_airframer.name), name='test_aircraft')
        test_aircraft.save()

    def test_access_api_without_credentials(self):

        #creation of the request
        response = self.client.post('http://localhost:8000/')

        #print(response)

        #response verification
        self.assertEqual(response.data, {"detail": "Authentication credentials were not provided."})

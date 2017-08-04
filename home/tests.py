from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentication.serializers import UserSerializer


class HomeAPITests(APITestCase):

    def setUp(self):
        user_dict = {
            'first_name': 'aamish',
            'last_name': 'baloch',
            'email': 'aamish@gmail.com',
            'username': 'aamishbaloch',
            'password': 'githubisawesome',
        }

        serializer = UserSerializer(data=user_dict)
        if serializer.is_valid():
            self.user = serializer.save()

        url = reverse('login')
        data = {
            "username": user_dict['username'],
            "password": user_dict['password'],
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.token = response.data['token']

    def test_create_account(self):
        """
        Ensure we can view our home.
        """
        url = reverse('home')
        response = self.client.get(url, None, format='json', HTTP_AUTHORIZATION='Bearer {}'.format(self.token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
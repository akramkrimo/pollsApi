from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase, APIClient

from polls import apiviews
# Create your tests here.

class TestPoll(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({"get": "list"})
        self.url = ["/polls/", "/polls/4", "/polls/4/choices/"]
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        #self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email = 'testuser@test.com',
            password = 'test159321'
        )

    def test_list(self):
        for url in self.url:
            request = self.factory.get(url, 
                HTTP_AUTHENTICATION='Token {}'.format(self.token.key))
            request.user = self.user
            response = self.view(request)
            self.assertEqual(response.status_code, 200,
            'Expected Response Code 200, received {0} instead'
            .format(response.status_code))

    def test_list2(self):
        self.client.login(username='test', password='test159321')
        response = self.client.get(self.url[0])
        self.assertEqual(response.status_code, 200,
                    'Expected Response Code 200, received {0} instead'
                    .format(response.status_code))

    def test_create(self):
        self.client.login(username='test', password='test159321')
        params = {
            "question": "how u doing?",
            "created_by": 1
        }
        response = self.client.post(self.url[0], params)
        self.assertEqual(response.status_code, 201,
                "Expected Response Code 201, received {0} instead"
                .format(response.status_code))

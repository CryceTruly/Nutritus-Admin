from rest_framework.test import APIClient ,APISimpleTestCase

class TestPoll(APISimpleTestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri=reversed('api/nutrients/')

# Create your tests here.
def test_list(self):
    response = self.client.get(self.uri)
    self.assertEqual(response.status_code, 200,
                     'Expected Response Code 200, received {0} instead.'
                     .format(response.status_code))
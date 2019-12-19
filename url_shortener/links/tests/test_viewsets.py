from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()


def test_post_link():
    request = factory.post('/links/', {'full_url': "https://google.com", })

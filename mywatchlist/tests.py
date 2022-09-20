from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.html_url = ("/mywatchlist/html/")
        self.json_url = ("/mywatchlist/json/")
        self.xml_url = ("/mywatchlist/xml/")

    def test_html_url(self):
        response = self.client.get((self.html_url))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "mywatchlist.html")

    def test_json_url(self):
        response = self.client.get((self.json_url))
        self.assertEquals(response.status_code, 200)

    def test_xml_url(self):
        response = self.client.get((self.xml_url))
        self.assertEquals(response.status_code, 200)

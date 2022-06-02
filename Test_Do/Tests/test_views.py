import unittest
import json

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from Test_Do.models import Note


class TestNoteListCreateAPIView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="test@test.ru")

    def test_list_objects(self):
        Note.objects.create(title="Test title", author_id=1)

        test_user = User.objects.get(username="test@test.ru")
        Note.objects.create(title="Test title", author=test_user)

        url = "/api/v1/notes/"
        resp = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        # response_data = resp.data
        # self.assertEqual(0, len(response_data))

    def test_empty_list_objects(self):
        url = "/api/v1/notes/"
        resp = self.client.get(url)

        expected_status_code = status.HTTP_200_OK
        self.assertEqual(expected_status_code, resp.status_code)

        response_data = resp.data
        expected_data = []
        self.assertEqual(expected_data, response_data)

    @unittest.skip("Еще не реализовано")
    def test_create_objects(self):
        # data = {"title":
        #        "test_title"}
        # json_data = json.dumps(data)
        url = "/api/v1/add/"
        resp = self.client.post("/api/v1/add/", data={"title": "new_title"}, format='json')
        # resp = self.client.post(url, json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, resp.status_code)
        #Note.objects.get(title="test_title")  # self.assertTrue(Note.objects.exists(title=new_title))


class TestNoteDetailAPIView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="test@test.ru")
        Note.objects.create(title="Test title", author_id=1)

    @unittest.skip("Еще не реализовано")
    def test_retrieve_object(self):
        note_pk_id = 1
        url = f"/api/v1/notes/{note_pk_id}"

        resp = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        expected_data = {
            "id": 1,
            "title": "Test title"
        }

        self.assertDictEqual(expected_data, resp.data)


    def test_does_not_exists_object(self):
        does_not_exist_pk = "12312341241234"
        url = f"/api/v1/notes/{does_not_exist_pk}"

        resp = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, resp.status_code)

    @unittest.skip("Еще не реализовано")
    def test_update_object(self):
        update_pk = 1
        url = f"/api/v1/edit/{update_pk}"
        resp = self.client.patch(url, data={"title": "new_title"}, format='json')
        self.assertEqual(status.HTTP_200_OK, resp.status_code)







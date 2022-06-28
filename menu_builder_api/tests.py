from django.urls import reverse
from rest_framework import status
from django.test import TestCase


class SectionTest(TestCase):
    def setUp(self):
        self.data = {'name': 'lunch special', 'description': 'lunch description'}
        self.data_update = {'name': 'lunch special', 'description': 'lunch description', "id": 1}

    def test_can_create_section(self):
        response = self.client.post(reverse('section'), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_section(self):
        response = self.client.get(reverse('section'))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_can_update_section(self):
    #     response = self.client.patch(reverse('section_id',  kwargs={'id': '1'}), self.data_update)
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_can_delete_section(self):
    #     response = self.client.delete(reverse('section_id',  kwargs={'id': '1'}), self.data_update)
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class ItemTest(TestCase):
    def setUp(self):
        self.data = {'name': 'soup lunch', 'description': 'soup lunch description', 'price': 23.0,
                     'section_id': 1, 'modifiers': ''}
        self.data_update = {'name': 'soup lunch', 'description': 'soup lunch description', "id": 1}

    # def test_can_create_items(self):
    #     response = self.client.post(reverse('items'), self.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_items(self):
        response = self.client.get(reverse('items'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_can_update_items(self):
    #     response = self.client.patch(reverse('item_id',  kwargs={'id': '1'}), self.data_update)
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_can_delete_items(self):
    #     response = self.client.delete(reverse('item_id',  kwargs={'id': '1'}), self.data_update)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class ModifierTest(TestCase):
    def setUp(self):
        self.data = {'modifiers_description': 'mike', 'items_id': 1}
        self.data_update = {'modifiers_description': 'mike', 'items_id': 1, "id": 1}

    def test_can_create_modifier(self):
        response = self.client.post(reverse('modifier'), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_modifier(self):
        response = self.client.get(reverse('modifier'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_can_update_modifier(self):
    #     response = self.client.patch(reverse('modifier_id',  kwargs={'id': '1'}), self.data_update)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_can_delete_modifier(self):
    #     response = self.client.delete(reverse('modifier_id',  kwargs={'id': '1'}), self.data_update)
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class ModifierItemsMappingTest(TestCase):
    def setUp(self):
        # self.data = {'name': 'mike', 'description': 'Mike'}
        self.url_user_list = ('http://127.0.0.1:8000/api/items-modifiers/')

    def test_can_create_modifier_items(self):
        response = self.client.get((self.url_user_list))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SectionCompleteTest(TestCase):
    def setUp(self):
        # self.data = {'name': 'mike', 'description': 'Mike'}
        self.data_update = {'name': 'mike', 'description': 'Mike', "id": 1}

    def test_can_get_section_data(self):
        response = self.client.get(reverse('section_data'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

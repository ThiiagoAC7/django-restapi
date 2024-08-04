from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken 
from django.contrib.auth.models import User
from .models import Task
from django.utils.timezone import make_aware

import datetime


class TaskTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.client = APIClient()

        token = RefreshToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
        
        self.test_task_1 = Task.objects.create(
            title="Tarefa de teste 1",
            description="Descrição da tarefa de teste 1",
            due_date=make_aware(datetime.datetime.now() + datetime.timedelta(days=1))
        )

        self.test_task_2 = Task.objects.create(
            title="Tarefa de teste 2",
            description="Descrição da tarefa de teste 2",
            due_date=make_aware(datetime.datetime.now() + datetime.timedelta(days=2))
        )
    

    def test_create_task(self):
        date = datetime.datetime.now() + datetime.timedelta(days=3)
        data = {
            "title": "Tarefa de teste 3",
            "description": "Descrição da tarefa de teste 3",
            "due_date": make_aware(date)
        }
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_update_task(self):
        date = datetime.datetime.now() + datetime.timedelta(days=1)
        data = {
            "title": "Tarefa de teste update",
            "description": "Descrição da tarefa de teste update",
            "due_date": make_aware(date)
        }

        response = self.client.put(f'/api/tasks/{self.test_task_1.id}/', data, format='json')

        self.assertEqual(response.status_code, 200)
        self.test_task_1.refresh_from_db()
        self.assertEqual(self.test_task_1.title, data['title'])
        self.assertEqual(self.test_task_1.description, data['description'])

    def test_filter_tasks_by_title(self):
        filter = "Tarefa de teste 2"
        response = self.client.get(f'/api/tasks/?title={filter}', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], filter)
    

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.test_task_2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.count(), 1)



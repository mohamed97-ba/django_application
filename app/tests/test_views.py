import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from EmployeeApp.models import Employee, Work_Arrangement
from EmployeeApp.serializers import EmployeeSerializer, Work_ArrangementSerializer


# initialize the APIClient app
client = Client()

class GetAllEmployeesTest(TestCase):
    """ Test module for GET all employees API """

    def setUp(self):
        Employee.objects.create(
            name="mohamed", team="DT", hourly_rate=20, is_team_leader=False
        )
        Employee.objects.create(
            name="hamza", team="RH", hourly_rate=30, is_team_leader=True
        )
        Employee.objects.create(
            name="ghada", team="DM", hourly_rate=15, is_team_leader=False
        )

    def test_get_all_employees(self):
        # get API response
        response = client.get(reverse('employees'))
        # get data from db
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class GetSingleEmployeeTest(TestCase):
    """ Test module for GET single employee API """

    def setUp(self):
        self.mohamed = Employee.objects.create(
            name="mohamed", team="DT", hourly_rate=20, is_team_leader=False
        )
        self.hamza = Employee.objects.create(
            name="hamza", team="RH", hourly_rate=30, is_team_leader=True
        )
        self.ghada = Employee.objects.create(
            name="ghada", team="DM", hourly_rate=15, is_team_leader=False
        )

    def test_get_valid_single_employee(self):
        response = client.get(
            reverse('employee', kwargs={'pk': self.mohamed.pk}))
        employee = Employee.objects.get(pk=self.mohamed.pk)
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_employee(self):
        response = client.get(
            reverse('employee', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
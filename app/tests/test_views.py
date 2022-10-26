import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from EmployeeApp.models import Employee, Work_Arrangement
from EmployeeApp.serializers import EmployeeSerializer, Work_ArrangementSerializer


# initialize the APIClient app
client = Client()


class GetAllEmployeesTest(TestCase):
    """Test module for GET all employees API"""

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

    def test_get_all_employees(self) -> None:
        # get API response
        response = client.get(reverse("employees"))
        # get data from db
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleEmployeeTest(TestCase):
    """Test module for GET single employee API"""

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

    def test_get_valid_single_employee(self) -> None:
        response = client.get(reverse("employee", kwargs={"pk": self.mohamed.pk}))
        employee = Employee.objects.get(pk=self.mohamed.pk)
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_employee(self) -> None:
        response = client.get(reverse("employee", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewEMployeeTest(TestCase):
    """Test module for inserting a new employee"""

    def setUp(self):
        self.valid_payload = {
            "name": "Med",
            "team": "DT",
            "hourly_rate": 20.0,
            "is_team_leader": True,
        }
        self.invalid_payload = {
            "name": "",
            "team": "DT",
            "hourly_rate": 20.0,
            "is_team_leader": True,
        }

    def test_create_valid_employee(self) -> None:
        response = client.post(
            reverse("employees"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_employee(self) -> None:
        response = client.post(
            reverse("employees"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleEmployeeTest(TestCase):
    """Test module for updating an existing employee object"""

    def setUp(self):
        self.mohamed = Employee.objects.create(
            name="mohamed", team="DT", hourly_rate=40, is_team_leader=False
        )
        self.hamza = Employee.objects.create(
            name="hamza", team="RH", hourly_rate=30, is_team_leader=True
        )
        self.valid_payload = {
            "name": "mohamed",
            "team": "DT",
            "hourly_rate": 25,
            "is_team_leader": True,
        }
        self.invalid_payload = {
            "name": "",
            "team": "DT",
            "hourly_rate": 15,
            "is_team_leader": False,
        }

    def test_valid_update_employee(self) -> None:
        response = client.put(
            reverse("employee", kwargs={"pk": self.mohamed.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_employee(self) -> None:
        response = client.put(
            reverse("employee", kwargs={"pk": self.hamza.pk}),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleEmployeeTest(TestCase):
    """Test module for deleting an existing job record"""

    def setUp(self):
        self.mohamed = Employee.objects.create(
            name="mohamed", team="DT", hourly_rate=40, is_team_leader=False
        )
        self.hamza = Employee.objects.create(
            name="hamza", team="RH", hourly_rate=30, is_team_leader=True
        )

    def test_valid_delete_employee(self) -> None:
        response = client.delete(reverse("employee", kwargs={"pk": self.mohamed.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_employee(self) -> None:
        response = client.delete(reverse("employee", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# test work_arragement models


class GetAlljobsTest(TestCase):
    """Test module for GET all employees API"""

    def setUp(self):
        Employee.objects.create(
            name="mohamed", team="DT", hourly_rate=20, is_team_leader=True
        )
        self.employee_1 = Employee.objects.get(name="mohamed")

        Work_Arrangement.objects.create(
            employee=self.employee_1, full_or_partime="FT", work_rate=100.0
        )
        Employee.objects.create(
            name="hamza", team="DT", hourly_rate=15, is_team_leader=False
        )
        self.employee_2 = Employee.objects.get(name="hamza")
        Work_Arrangement.objects.create(
            employee=self.employee_2, full_or_partime="PT", work_rate=50.0
        )

    def test_get_all_jobs(self) -> None:
        # get API response
        response = client.get(reverse("jobs"))
        # get data from db
        jobs = Work_Arrangement.objects.all()
        serializer = Work_ArrangementSerializer(jobs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleJobTest(TestCase):
    """Test module for GET single employee API"""

    def setUp(self):
        Employee.objects.create(
            name="mohamed", team="DT", hourly_rate=20, is_team_leader=True
        )
        self.employee_1 = Employee.objects.get(name="mohamed")

        self.job1 = Work_Arrangement.objects.create(
            employee=self.employee_1, full_or_partime="FT", work_rate=100.0
        )
        Employee.objects.create(
            name="hamza", team="DT", hourly_rate=15, is_team_leader=False
        )
        self.employee_2 = Employee.objects.get(name="hamza")
        self.job2 = Work_Arrangement.objects.create(
            employee=self.employee_2, full_or_partime="PT", work_rate=50.0
        )

    def test_get_valid_single_job(self) -> None:
        response = client.get(reverse("job", kwargs={"pk": self.job1.pk}))
        job = Work_Arrangement.objects.get(pk=self.job1.pk)
        serializer = Work_ArrangementSerializer(job)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_employee(self) -> None:
        response = client.get(reverse("job", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DeleteSingleJobTest(TestCase):
    """Test module for deleting an existing job"""

    def setUp(self):
        Employee.objects.create(
            name="mohamed", team="DT", hourly_rate=20, is_team_leader=True
        )
        self.employee_1 = Employee.objects.get(name="mohamed")

        Work_Arrangement.objects.create(
            employee=self.employee_1, full_or_partime="FT", work_rate=100.0
        )
        Employee.objects.create(
            name="hamza", team="DT", hourly_rate=15, is_team_leader=False
        )
        self.employee_2 = Employee.objects.get(name="hamza")
        self.job2 = Work_Arrangement.objects.create(
            employee=self.employee_2, full_or_partime="PT", work_rate=50.0
        )

    def test_valid_delete_job(self) -> None:
        response = client.delete(reverse("job", kwargs={"pk": self.job2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_job(self) -> None:
        response = client.delete(reverse("job", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class SalaryTest(TestCase):
    """Test module for employe salary"""

    def setUp(self):
        Employee.objects.create(
            name="mohamed", team="DT", hourly_rate=20, is_team_leader=False
        )
        Employee.objects.create(
            name="hamza", team="DT", hourly_rate=0, is_team_leader=False
        )
        self.employee_1 = Employee.objects.get(name="mohamed")
        self.employee_2 = Employee.objects.get(name="hamza")
        Work_Arrangement.objects.create(
            employee=self.employee_1, full_or_partime="FT", work_rate=100.0
        )
        Work_Arrangement.objects.create(
            employee=self.employee_2, full_or_partime="FT", work_rate=100.0
        )

    def test_pay_month(self) -> None:
        response = client.get(reverse("pay_month", kwargs={"pk": self.employee_1.pk}))
        self.assertEqual(response.json(), {"Salary": 3200})

    def test_invalid_pay_month(self) -> None:
        response = client.get(reverse("pay_month", kwargs={"pk": self.employee_2.pk}))
        self.assertEqual(response.json(), {"Salary": 0})

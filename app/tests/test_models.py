from django.test import TestCase
from EmployeeApp.models import Employee, Work_Arrangement


class EmployeeTest(TestCase):
    """Test module for Employee model"""

    def setUp(self):
        Employee.objects.create(
            name="mohamed", team="DT", hourly_rate=20, is_team_leader=True
        )
        Employee.objects.create(
            name="hamza", team="DT", hourly_rate=15, is_team_leader=False
        )

    def test_employee(self):
        employee_mohamed = Employee.objects.get(name="mohamed")
        employee_hamza = Employee.objects.get(name="hamza")
        self.assertEqual(
            employee_mohamed.get_employee(), "mohamed belongs to DATA team."
        )
        self.assertEqual(employee_hamza.get_employee(), "hamza belongs to DATA team.")


class Work_ArrangementTest(TestCase):
    """Test module for work_arrangement model"""

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

    def test_work_arrangement(self):
        job1 = Work_Arrangement.objects.get(employee_id=self.employee_1.pk)
        job2 = Work_Arrangement.objects.get(employee_id=self.employee_2.pk)
        self.assertEqual(job1.__str__(), "mohamed is a 100.0 FULLTIME")
        self.assertEqual(job2.__str__(), "hamza is a 50.0 PARTIME")

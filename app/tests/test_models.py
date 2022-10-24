from django.test import TestCase
from EmployeeApp.models import Employee


class EmployeeTest(TestCase):
    """ Test module for Employee model """

    def setUp(self):
        Employee.objects.create(
            name='mohamed', team='DT', hourly_rate=20, is_team_leader=True)
        Employee.objects.create(
            name='hamza', team='DT', hourly_rate=15, is_team_leader=False)

    def test_employee(self):
        employee_mohamed = Employee.objects.get(name='mohamed')
        employee_hamza = Employee.objects.get(name='hamza')
        self.assertEqual(
            employee_mohamed.get_employee(), "mohamed belongs to DATA team.")
        self.assertEqual(
            employee_hamza.get_employee(), "hamza belongs to DATA team.")
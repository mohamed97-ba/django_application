from django.db import models
from django.forms import CharField

from .utils import WorkType, Team


class Employee(models.Model):
    """

    Employee Model:
    Defines the attributes of an Employee
    """

    name = models.CharField(max_length=100)
    team = models.CharField(max_length=2, choices=Team.choices(), default=Team.DATA)
    hourly_rate = models.FloatField(null=False)
    is_team_leader = models.BooleanField()

    def get_employee(self) -> str:
        return self.name + " belongs to " + self.get_team_name() + " team."

    def get_team_name(self) -> str:
        return Team(self.team).name


class Work_Arrangement(models.Model):
    """

    Work_Arrangement Model:
    Defines the attributes of work_arrangement
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    full_or_partime = models.CharField(
        max_length=2, choices=WorkType.choices(), default=WorkType.FULLTIME
    )  # type: str
    work_rate = models.FloatField()  # type: float

    def get_work_type(self) -> str:
        return WorkType(self.full_or_partime).name

    def __str__(self) -> str:
        return (
            self.employee.name
            + " is a "
            + str(self.work_rate)
            + " "
            + self.get_work_type()
        )

    @staticmethod
    def get_jobs_by_employee(employee_id):
        return Work_Arrangement.objects.all().filter(employee=employee_id)

from django.http import JsonResponse
from yaml import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Employee, Work_Arrangement
from .serializers import EmployeeSerializer, Work_ArrangementSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def employee_detail(request, pk):
    '''
    @GET: get details of an employee object
    '''
    try:
        employee = Employee.objects.get(pk=pk)
    except employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    # update details of a single puppy
    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single puppy
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def employee_list(request):
    # get all employees
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    # insert a new object for an employee
    if request.method == 'POST':

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def work_detail(request, pk):
    '''
    @GET: get details of a work arrangement
    '''
    try:
        job = Work_Arrangement.objects.get(pk=pk)
    except job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Work_ArrangementSerializer(job)
        return Response(serializer.data)

    # update details of a single puppy
    if request.method == 'PUT':
        serializer = Work_ArrangementSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single puppy
    if request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def work_list(request, format=None):
    # get all employees
    if request.method == 'GET':
        jobs = Work_Arrangement.objects.all()
        serializer = Work_ArrangementSerializer(jobs, many=True)
        return Response(serializer.data)
    # insert a new object for an employee
    if request.method == 'POST':
        serializer = Work_ArrangementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def Salary(request, pk):
    if request.method == 'GET':
        employee = Employee.objects.get(pk=pk)
        jobs = Work_Arrangement.get_jobs_by_employee(employee)
        pay_month = 0
        for job in jobs:
            if job.full_or_partime == "FT":
                if employee.is_team_leader == False:
                    pay_month = (employee.hourly_rate * 40) * 4

                else:
                    pay_month = (employee.hourly_rate * 40) * 4
                    pay_month = pay_month + pay_month * 10 / 100
            else:
                if employee.is_team_leader == False:
                    pay_month += job.work_rate * 0.4 * employee.hourly_rate * 4
                else:

                    pay_month = job.work_rate * 0.4 * employee.hourly_rate * 4
                    pay_month += pay_month * 10 / 100
        return JsonResponse({"Salary": pay_month}, safe=False)

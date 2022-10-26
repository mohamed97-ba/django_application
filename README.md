# CRUD API WITH DJANGO REST FRAMEWORK
a company's employee management system crud application which lets the company's accountant retrieve the list of employees with their respective
pay for the month.

## Requirements
- Python 
- Django 
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

You can install all the required dependencies by running
```
pip install -r requirement.txt
```

## Structure

In our case, `Employee`, `Work_Arrangement`, so we will use the following URLS - `/employees/`, `/employees/<pk>`, `/jobs/`, `jobs/:pk` and `salary/:pk` respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`employees, jobs` | GET | READ | Get all employees, jobs
`employees/:pk, jobs/:pk`| GET | READ | Get a single employee, single job
`employees, jobs`| POST | CREATE | Create a new employee, new job
`employees/:pk, jobs/:pk`| PUT | UPDATE | Update an employee, job
`employees/:pk, jobs/:pk`| DELETE | DELETE | Delete an employee, job
`salary/:pk`| GET | READ | Get the pay_month


## Use
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation), or we can use [Postman](https://www.postman.com/)


First, we have to start up Django's development server.
```
python manage.py runserver 8001
```
Only authenticated users can use the API services, for that reason if we try this:
```
curl  http://127.0.0.1:8001/employees
curl  http://127.0.0.1:8001/jobs
curl  http://127.0.0.1:8001/salary/1/
curl  http://127.0.0.1:8001/salary/2/

```
we get:
```
[{"id":1,"name":"mohamed","team":"DT","hourly_rate":20.0,"is_team_leader":true},{"id":2,"name":"hamza","team":"DT","hourly_rate":15.0,"is_team_leader":false}]
[{"id":1,"full_or_partime":"FT","work_rate":100.0,"employee":1},{"id":2,"full_or_partime":"PT","work_rate":30.0,"employee":2},{"id":3,"full_or_partime":"PT","work_rate":70.0,"employee":2}]
{"Salary": 3520.0}
{"Salary": 2400.0}
```

we get the employee with id = 1
we get the jobs with id = 1

```
{"id":1,"name":"mohamed","team":"DT","hourly_rate":20.0,"is_team_leader":true}
{"id":1,"full_or_partime":"FT","work_rate":100.0,"employee":1}
```



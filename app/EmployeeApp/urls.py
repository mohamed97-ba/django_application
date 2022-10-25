from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path(
        'employees',
        views.employee_list
    ),
    path('employees/<int:pk>/', views.employee_detail),
    path(
        'jobs',
        views.work_list
    ),
    path(
        'jobs/<int:pk>/',
        views.work_detail
    ),
    path(
        'salary/<int:pk>/',
        views.Salary
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)

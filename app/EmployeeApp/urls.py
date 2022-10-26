from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("employees", views.employee_list, name="employees"),
    path("employees/<int:pk>/", views.employee_detail, name="employee"),
    path("jobs", views.work_list, name="jobs"),
    path("jobs/<int:pk>/", views.work_detail, name="job"),
    path("salary/<int:pk>/", views.Salary, name="pay_month"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls.static import static
from django.urls.conf import re_path
from EmployeeApp import views
from django.conf import settings
urlpatterns = [
    re_path(r'^department/$',views.DepartmentApi),
    re_path(r'^department/([0-9]+)$',views.DepartmentApi),
    re_path(r'^employee/$',views.EmployeeApi),
    re_path(r'^employee/([0-9]+)$',views.EmployeeApi),
    re_path(r'^SavePhoto$',views.SavePhoto)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

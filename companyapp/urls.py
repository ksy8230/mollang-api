from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from companyapp.views import RegisterCompany, CompanyList, UpdateCompany

app_name = "companyapp"

urlpatterns = [
    path('register/', RegisterCompany.as_view(), name='register'),
    path('update/', UpdateCompany.as_view(), name='update'),
    path('list/', CompanyList.as_view(), name='list'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from companyapp.views import RegisterCompany, CompanyList, UpdateCompany, CompanyList_Review_Write

app_name = "companyapp"

urlpatterns = [
    path('register/', RegisterCompany.as_view(), name='register'),
    path('update/<int:pk>', UpdateCompany.as_view(), name='update'),
    path('delete/<int:pk>', UpdateCompany.as_view(), name='update'),
    path(r'list', CompanyList.as_view(), name='list'),
    path(r'listWrite', CompanyList_Review_Write.as_view(), name='listWrite'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

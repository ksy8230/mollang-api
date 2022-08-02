from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from reviewapp.views import RegisterReview, ReviewList

app_name = "reviewapp"

urlpatterns = [
    path('register/', RegisterReview.as_view(), name='register'),
    path(r'list', ReviewList.as_view(), name='list'),
    # path('update/<int:pk>', UpdateCompany.as_view(), name='update'),
    # path('delete/<int:pk>', UpdateCompany.as_view(), name='update'),
    # path(r'list', CompanyList.as_view(), name='list'),
    # path(r'listWrite', CompanyList_Review_Write.as_view(), name='listWrite'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

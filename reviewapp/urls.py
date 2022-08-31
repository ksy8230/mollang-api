from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from reviewapp.views import RegisterReview, ReviewList, UpdateReview, RegisterComment

app_name = "reviewapp"

urlpatterns = [
    path('register/', RegisterReview.as_view(), name='register'),
    path(r'list', ReviewList.as_view(), name='list'),
    path('<int:pk>', UpdateReview.as_view(), name='detail'),
    path('<int:pk>/comments/', RegisterComment.as_view(), name='register_comment'),
    path('comments/<int:comment_pk>/', RegisterComment.as_view(), name='update_comment'),
    path('comments/delete/<int:comment_pk>/', RegisterComment.as_view(), name='delete_comment'),
    # path('update/<int:pk>', UpdateCompany.as_view(), name='update'),
    # path('delete/<int:pk>', UpdateCompany.as_view(), name='update'),
    # path(r'list', CompanyList.as_view(), name='list'),
    # path(r'listWrite', CompanyList_Review_Write.as_view(), name='listWrite'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

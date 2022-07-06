from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from articleapp.views import ArticleList

urlpatterns = [
    path('article/', ArticleList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

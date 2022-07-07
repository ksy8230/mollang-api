from django.urls import path
from accountapp.views import hello_world, Login, AccountList

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', Login.as_view(), name='login'),
    path('register/', AccountList.as_view(), name='register')
]

from django.urls import path
from accountapp.views import hello_world, Login, CreateAccount, AccountList

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', Login.as_view(), name='login'),
    path('register/', CreateAccount.as_view(), name='register'),
    path('user_list/', AccountList.as_view(), name='user_list')
]

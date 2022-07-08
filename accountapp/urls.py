from django.urls import path
from accountapp.views import hello_world, Login, Account, AccountList, WhoIam

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Account.as_view(), name='register'),
    path('whoIam/', WhoIam.as_view(), name='whoIam'),
    path('user_list/', AccountList.as_view(), name='user_list')
]

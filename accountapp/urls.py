from django.urls import path
from accountapp.views import hello_world, Login, Logout, Account, AccountList, WhoIam, UpdateAccount

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Account.as_view(), name='register'),
    path('whoIam/', WhoIam.as_view(), name='whoIam'),
    path('updateUser/', UpdateAccount.as_view(), name='UpdateAccount'),
    path('user_list/', AccountList.as_view(), name='user_list')
]

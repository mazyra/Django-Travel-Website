from django.urls import path
from accounts.views import login, signup

app_name = 'accounts'

urlpatterns = [
    #login
    path('login', login, name='login'),
    #logout
    #####
    #register
    path('signup', signup, name='signup'),
]
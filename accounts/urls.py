from django.urls import path
from accounts.views import login_view, signup_view

app_name = 'accounts'

urlpatterns = [
    #login
    path('login', login_view, name='login'),
    #logout
    #####
    #register
    path('signup', signup_view, name='signup'),
]
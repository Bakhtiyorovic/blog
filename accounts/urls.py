from django.urls import path
from .views import *
from django.urls import path
from .views import logout_view

urlpatterns = [
    path('singup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
]
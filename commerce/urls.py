from django.urls import path
from .views import Regsiter, Login, Dashboard, Logout

urlpatterns = [
    path("register/", Regsiter.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"), 
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
]
from django.urls import path
from . import views

app_names = "user"
urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout")
]
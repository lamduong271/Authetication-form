from django.urls import path, include
from . import views
app_name = "news"
urlpatterns = [
    path('', views.LoginClass.as_view(), name="index"),
]
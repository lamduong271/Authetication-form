from django.urls import path, include
from . import views
app_name = "login"
urlpatterns = [
    path('', views.LoginClass.as_view(), name="index"),
    path('permission/', views.ViewUser.as_view(), name="permission"),
    path('product/', views.view_product, name="product"),
    path('article/', views.AddArticle.as_view(), name="article"),
]
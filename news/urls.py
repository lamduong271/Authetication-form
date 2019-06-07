from django.urls import path, include
from . import views
app_name = "news"
urlpatterns = [
    path('', views.indexClass.as_view(), name="index"),
    # path('add-post/', views.addPostClass.as_view(), name="add_post"),
    path('add-post/save/', views.save_news.as_view(), name="save_news"),
    path('send_email/', views.email_view, name="email_view"),
    path('send_email/save', views.email_sent, name="send_email")
]
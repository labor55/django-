from django.conf.urls import include, url
from comment import views

urlpatterns = [
    url(r'^comment_blog(\d+)/$', views.comment_blog),
    ]
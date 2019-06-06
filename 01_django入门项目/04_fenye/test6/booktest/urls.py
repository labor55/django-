
from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^area/$', views.area),
    url(r'^send/$', views.send),
    url(r'^pic_show/$', views.pic_show),
    url(r'^pic_upload/$', views.pic_upload),
    url(r'^pic_chu/$', views.pic_chu),
    url(r'^area_show/$', views.area_show),
    url(r'^area_show2/$', views.area_show2),
    url(r'^area_show3_(\d+)/$', views.area_show3),
    url(r'^blog_list/$', views.blog_list),
    url(r'^blog_detail/(\d+)/$', views.blog_detail,name='detail'),
]

from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index$', views.index),
    # 传递参数以及顺序
    # url(r'^delete/(\w+)/(\d+)$',views.delete),
    # 给参数取别名，顺序随意
    url(r'^delete/(?P<str1>\w+)/(?P<id1>\d+)$',views.delete),
    url(r'^method_show/$', views.method_show),
    url(r'^arg_show/$', views.arg_show),

    url(r'^ajax1/$', views.ajax1),
    url(r'^ajax2/$', views.ajax2),
    url(r'^redi/$', views.redi),

    url(r'^cookie_set/$', views.cookie_set),
    url(r'^cookie_get/$', views.cookie_get),

    url(r'^index1/$', views.index1),
    url(r'^detail/(\d+)/$', views.detail),

    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^session_del/$', views.session_del),
]

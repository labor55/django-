from django.conf.urls import include, url
from login import views

urlpatterns = [
	# 主页面
    url(r'^$', views.index),
    # 登陆信息确认
    url(r'login_check',views.login_check),
    # 登录后的界面
    url(r'success', views.success),
    # HttpResponse 传递字符（标签可以直接被渲染成h5）
    url(r'^index2/$',views.index2),
    # 调用模板
    url(r'^index3/$',views.index3),
    # json
    url(r'^json1/$',views.json1),
    url(r'^json2/$',views.json2),
    # 设置cookie
    # url(r'^cookie_set/$',views.cookie_set),
    # set有bug 
    url(r'^cookie_set/$',views.cookie_set),
    url(r'^cookie_get/$',views.cookie_get),

    # 设置session
    url(r'^session_test/$',views.session_test),
    
]

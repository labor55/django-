from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    # 首页
    url(r'^$', views.index),
    # 传递参数
    url(r'^temp_var$', views.temp_var),
    # 传递标签
    url(r'^temp_tags$', views.temp_tags),
    # 使用过滤器
    url(r'^temp_filter$', views.temp_filter),
    # HTML继承
    url(r'^temp_inherit$', views.temp_inherit),
    url(r'^temp_inherit_son$', views.temp_inherit_son),
    
    # 转义
    url(r'^html_zhuan/$', views.html_zhuan),
    # 不专义引起的xss攻击/使用ie打开
    url(r'^xss_test/$', views.xss_test),

    # 生成验证码和显示验证码
    url(r'^verify_code/$', views.verify_code),
    url(r'^verify_show/$', views.verify_show),
    # 验证码验证/取别名，让修改更方便
    url(r'^verify_yz/$', views.verify_yz, name='haha'),

    # 反向解析
    url(r'^fan1/$', views.fan1, name='fan1'),
    url(r'^fan2/$', views.fan2, name='fan2'),

]



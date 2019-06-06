1、分页

```shell
# 分页函数
# p= Paginator(area,5)
# p.num_pages 表示一共分出多少页
# p.page_range 分页器的range属性, 可以用来迭代

# page1 = p.page(1) 获得第一页内容
# page1.number 获取当前页是第几页
# page1.object_list 获得当前页的所有对象
# page1.paginator 查看页面所属的分页器对象
# page1.has_next() 查看是否有下一页True/False
# page1.has_next() 查看是否有上一页True/False
# page1.previous_page_number() #获取上一页的页码
# page1.next_page_number() #获取下一页的页码
```

2、发送邮件

```python
# 发送邮箱的配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'  # 163邮箱服务器地址
EMAIL_PORT = 25 # smtp端口

# 发送邮件的邮箱
EMAIL_HOST_USER = *******@163.com'

# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = '*********'
# 收件人看到的发件人(代理)
EMAIL_FROM = 'python<******@163.com>'
```



3、上传图片

```python
# 上传图片的配置路径
MEDIA_ROOT = os.path.join(BASE_DIR,'static/media')

<form action='/pic_chu/' method='post' enctype="multipart/form-data"> </form>
```

4、选择框

5、中间件

在settings.py----MIDDLEWARE_CLASSES中，添加路径

```python
class MyMid():
	# 服务器响应的第一个请求的时候调用一次
	def __init__(self):
		print("*"*30+"服务器初始化")

	# 此函数执行先于urls匹配，request请求先一步发送给此函数
	def process_request(self,request):
		print("*"*30+"处理request请求之前")

	# 此函数先于view视图之前，匹配urls之后先把参数给此函数
	def process_view(self,request,view_fun,*view_args,**view_kwargs):
		print("*"*30+"处理view之前")

	# 响应给客户端之前，参数先一步给此函数执行
	def process_response(self,request,response):
		print("*"*30+"返回response之前")
		# 在这里设置cookie，可以使用户不管点击服务器哪个网址，都会带上cookie
		# set_cookie 
		return response
   
# 异常处理：先注册的后执行
class Excp1：
	def process_exception(self,request,exception):
		print(print("*"*30+"出现异常1"))

class Excp2：
	def process_exception(self,request,exception):
		print(print("*"*30+"出现异常2"))
```

6、自定义后台admin选项
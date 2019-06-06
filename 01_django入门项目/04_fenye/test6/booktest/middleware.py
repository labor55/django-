from django.shortcuts import HttpResponse

# 黑名单
black_list = []
# 对所有请求都生效
class MyMid():

	# 服务器响应的第一个请求的时候调用一次
	def __init__(self):
		print("*"*30+"服务器初始化")

	# 此函数执行先于urls匹配，request请求先一步发送给此函数
	def process_request(self,request):
		# 拿到请求端的ip，判断是否在黑名单中
		if request.META.get('REMOTE_ADDR') in black_list:
			return HttpResponse('<h1>你已经被我们拉黑了</h1>')
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
class Excp1:
	def process_exception(self,request,exception):
		print(print("*"*30+"出现异常1"))

class Excp2:
	def process_exception(self,request,exception):
		print(print("*"*30+"出现异常2"))
from django.shortcuts import render
from login.models import Account
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader


# Create your views here.

def success(request):
	# 返回自定义的H5界面
	return render(request,'login/success.html')

def index2(request):
	str = '<h1>hello world</h1>'
	# 直接返回响应，不需要html文件包装
	return HttpResponse(str)

def index(request):
	acc = Account.objects.all()
	# 传递数据到H5页面
	return render(request,'login/index.html',context={'acc':acc})


def login_check(request):
	name = request.POST.get('uname')
	pswd = request.POST.get('pswd')
	acc = Account.objects.all()
	print(acc)
	# 从数据库中对比用户账户的正确性
	for i in acc:
		if name == i.user and pswd == i.pwd:
			return JsonResponse({'res':1})
		else:
			return JsonResponse({'res':0})


# 使用render就足够了，比render繁琐
def index3(request):
	# 加载模版
	t1 = loader.get_template('login/index3.html')
	# 构造上下文
	context = RequestContext(request,{'h1':'hello'})
	# 使用上下文渲染模板，生成字符串之后返回相应对象
	return HttpResponse(t1.render(context))

# 传递json数据
def json1(request):
    return render(request,'login/json1.html')
def json2(request):
    return JsonResponse({'h1':'hello','h2':'world'})


# def cookie_set(request):
# 	response = HttpResponse("<h1>设置Cookie，查看响应报文头</h1>")
# 	response.set_cookie('h1','你好')
# 	return response

def cookie_set(request):
    response = HttpResponse("<h1>设置Cookie，请查看响应报文头</h1>")
    response.set_cookie('h1','ki')
    return response

def cookie_get(request):
	response = HttpResponse("读取cookie，数据如下: <br>")
	if 'h1' in request.COOKIES:
		response.write('<h1>' + request.COOKIES['h1'] + '</h1>')
	else:
		response.write('<h1>' + 'cookie不存在' + '</h1>')
	return response



def session_test(request):
	# 读取session
	h1=request.session.get('h1')
	# 如果session不存在，就创建一个session
	if not h1:
		request.session['h1'] = 'hello'
		# 30s 后过期
		request.session.set_expiry(30)
		# 标志位为true
		flag = 1
	# 如果session存在，就不改变
	else:
		# 标志位为false
		flag = 0
	return render(request,'login/comments.html',context={'flag':flag})

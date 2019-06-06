from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from booktest.models import Blog

# Create your views here.
def index(request):
    str1 = request.path
    str2 = request.encoding
    if request.session.has_key('isLogin'):
        flag = 1
    else:
        flag = 0
    return render(request, 'booktest/index.html', {'str1': str1, 'str2': str2,'flag':flag})

def delete(request,str1,id1):

	return HttpResponse(f'参数{str1},{id1}')

def method_show(request):
	# 跨域请求伪造
	return HttpResponse(request.method)


def arg_show(request):
	if request.method == 'GET':
	# 获取提交过程中get请求的数据
	# a=1&b=2&c=abc GET获得类似于字典的东西
		a = request.GET.get('a')
		b = request.GET.get('b')
		c = request.GET.get('c')
		return render(request,'booktest/arg_show.html',{'a':a,'b': b,'c':c})
	else:
		name = request.POST.get('uname')
		pwd = request.POST.get('pswd')
		likes = request.POST.getlist('like') 
		return render(request,'booktest/postarg.html',{'name':name,'pwd':pwd,'likes':likes})

def ajax1(request):
	return render(request,'booktest/ajax1.html')


def ajax2(request):
	return JsonResponse({'h1':'hello','h2':'world'})

def redi(request):

	return redirect('/')

def cookie_set(request):
	# 发给客户端
	res = HttpResponse('设置cookie')
	res.set_cookie('name','haha',60)
	return res

def cookie_get(request):
	# 客户端获取
	cookie = request.COOKIES.get('name')
	res = HttpResponse(f'cooike值：{cookie}')
	return res

def index1(request):
	blogs = Blog.objects.all()
	return render(request,'booktest/index1.html',{'blogs':blogs})

def detail(request,num):
	blog = Blog.objects.get(id=num)
	lab=request.session.get('lab')
	if not lab:
		request.session['lab']='haha'
		request.session.set_expiry(10)
		blog.read += 1
		blog.save()
	return render(request,'booktest/detail.html',{'blog':blog})

# def detail(request,id):
# 	blog = blog = Blog.objects.get(id=id)
# 	res = render(request,'booktest/detail.html',{'blog':blog})
# 	if not request.COOKIES.get(f'read{id}'):
# 		blog.read += 1
# 		blog.save()
# 		res.set_cookie(f'read{id}','1',60*60)
# 	return res


def session_del(request):
	# 指定键，删除session
	# del request.session['name']

	# clear 不需要指定具体键，只删除键值对
	request.session.clear()

	# 删除整条内容
	request.session.flush()
	return HttpResponse('ok')

def login(request):
    if request.session.has_key('isLogin'):
        # 表示已经登录了
        return redirect('/')
    else:
        # 用户未登录
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
        else:
            username = ''
    return render(request, 'booktest/login.html', {'username': username})


def login_check(request):
    '''登录校验'''
    username = request.POST.get('uname')
    password = request.POST.get('pswd')
    remember = request.POST.get('remember')

    if username == 'cxk' and password == '123':
        # 用户名，密码正确
        response = redirect('/')
        if remember == 'on':
            response.set_cookie('username', username, 60 * 60 * 24 * 14)
        request.session['isLogin'] = True
        return response
    else:
        # 用户名或者密码错误
        return redirect('/login')



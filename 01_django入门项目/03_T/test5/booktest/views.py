from django.shortcuts import render, HttpResponse
from booktest.models import BookInfo
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
# Create your views here.

# 首页视图
def index(request):
	return render(request,'booktest/index.html')


# 向HTML文件中传递参数
def temp_var(request):
	dict1 = {'title':'haha'}
	list1 = [1,2,3,4]
	books = BookInfo.objects.all()[0]

	return render(request,'booktest/temp_var.html',{'dict1':dict1,'list1':list1,'books':books})

# 标签
def temp_tags(request):
	books = BookInfo.objects.all()
	return render(request,'booktest/temp_tags.html',{'books':books})

# 过滤器
def temp_filter(request):
	books = BookInfo.objects.all()
	return render(request,'booktest/temp_filter.html',{'books':books})

# 继承
def temp_inherit(request):
	return render(request,'booktest/temp_inherit.html')
def temp_inherit_son(request):
	books = BookInfo.objects.all()
	return render(request,'booktest/temp_inherit_son.html',{'books':books})

# 模板转义 不转义会引起xss攻击
def html_zhuan(request):
	return render(request,'booktest/html_zhuan.html',{'content':'<h1>hello world</h1>'})

# xss攻击
def xss_test(request):
    text = ''
    if request.method == 'POST':
        text = request.POST.get('text')
    return render(request, 'booktest/xss.html', {'text': text})


# 生成验证码
def verify_code(request):
	import random
	# 背景色(偏蓝)，宽，高
	bgcolor = (random.randrange(20, 100),random.randrange(20, 100), 255)
	width = 100
	height = 25

	# 创建画面对象
	im = Image.new('RGB', (width, height), bgcolor)
	# 创建画笔对象
	draw = ImageDraw.Draw(im)
	# 调用画笔的point()函数绘制噪点(绘制100个噪点)
	for i in range(1, 100):
		xy = (random.randrange(0,width), random.randrange(0, height))
		fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
		draw.point(xy, fill=fill)
	# 定义验证码的备选值
	str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
	rand_str = ''
	for i in range(0,4):
		rand_str += str1[random.randrange(0, len(str1))]

	# 构造字体对象，
	font = ImageFont.truetype('static/font/MicroExtendFLF.ttf', 23)
	# 构造字体颜色（偏红）
	fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
	
	# 绘制四个字
	draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
	draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
	draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
	draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
	# 释放画笔
	del draw
	# 存入session 用于做进一步的验证
	request.session['verifycode'] = rand_str

	buf = BytesIO()
	im.save(buf, 'png')
	return HttpResponse(buf.getvalue(), 'image/png')

# 验证码显示
def verify_show(request):
	return render(request, 'booktest/verify_show.html')

# 验证码验证
def verify_yz(request):
	# 获取用户输入
	yzm = request.POST.get('yzm')
	if yzm == '':
		response=HttpResponse('no')
	
	# 获取服务器session
	verifycode = request.session['verifycode'].lower()
	response=HttpResponse('no')
	if yzm.lower()==verifycode:
		# 登陆成功
		response=HttpResponse('ok')
	return response


# 反向解析
def fan1(request):
	return render(request,'booktest/fan1.html')

def fan2(request):
	return HttpResponse('fan2')
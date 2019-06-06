from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from booktest.models import AreaInfo, PicTest, Blog
from django.conf import settings
from django.http import JsonResponse
from comment.forms import CommentForm
from comment.models import Comments
from django.views.decorators.cache import cache_page


# Create your views here.

def index(request):
	# 可以打印出对方的ip地址
	print(request.META.get('REMOTE_ADDR'))
	
	return HttpResponse('ok')

def blog_list(request):
	blogs = Blog.objects.all()
	context = {'blogs': blogs}
	return render(request,'booktest/blog_list.html',context)

#@cache_page(60*15)
def blog_detail(request, id=id):
	# 找到id对应的blog
	blog = Blog.objects.get(id=id)
	# 生成一个表单对象
	form = CommentForm()

	context = {'blog':blog, 'form':form}
	response = render(request, 'booktest/blog_detail.html', context)
	if not request.COOKIES.get(f'read{id}'):
		blog.read += 1
		blog.save()
		response.set_cookie(f'read{id}',1,60)
	return response

# 分页函数
# p= Paginator(area,5) 将对象area分成5页
# p.num_pages 表示一共分出多少页
# p.page_range 分页器的range属性, 可以用来迭代

# page1 = p.page(1) 获得第一页内容
# page1.number 获取当前页是第几页
# page1.object_list 获得当前页的所有对象
# page1.paginator 查看页面所属的分页器对象(总分页对象)
# page1.has_next 查看是否有下一页True/False
# page1.has_previous 查看是否有上一页True/False
# page1.previous_page_number #获取上一页的页码
# page1.next_page_number #获取下一页的页码

# https://127.0.1:8000/area/?page=3
def area(request):
	# 查找省份信息
	areas_list = AreaInfo.objects.filter(aParent__isnull=True)
	# 将省份分页，每页5条数据
	p= Paginator(areas_list,3)
	# 根据页码获取第几页的数据
	# 拿到请求的页数，设置默认值为1

	page_num = request.GET.get('page',1)
		# 格式转换
	now_num = int(page_num)

	

	# 自定义一个页码用来显示，（最多只显示5页）
	page_range = list(range(max(now_num-2,1),now_num))+list(range(now_num,min(p.num_pages,now_num+2)+1))

	# 折叠页数,用。。。来显示
	if page_range[0]-1>2:
		page_range.insert(0,'...')

	if p.num_pages - page_range[-1]>2:
		page_range.append('...')

	# 显示首页和尾页
	if page_range[0] != 1:
		page_range.insert(0,1)
	if page_range[-1] != p.num_pages:
		page_range.append(p.num_pages)

	# 获取页面的内容
	page = p.page(now_num)

	# num_str = request.POST.get('rearch')
	# if num_str != '':
	# 	now_num = int(num_str)
	return render(request, 'booktest/area.html',{'page':page, 'page_range':page_range})
	

# 发送邮件--settings.py设置服务器账号和授权码
def send(request):
	from django.core.mail import send_mail
	
	# 标签
	html_message = '<a href="http://127.0.0.1:8000/">点击激活</a>'

	try:
		# 主题 + 内容 + 代理名 + 收件人 + + 内容（标签优先） + 你的邮箱（false为默认本地设置的邮箱）
		send_mail('激活邮件','这是来自django的邮件',settings.EMAIL_FROM,['1337043202@qq.com'],html_message=html_message,fail_silently=False)
	except Exception as e:
		return HttpResponse(e)
	else:
		return HttpResponse('ok')
	
# 展示图片
def pic_show(request):
	imgs = PicTest.objects.all()
	return render(request,'booktest/pic_show.html',{'imgs':imgs})

# 图片上传页面
def pic_upload(request):
	return render(request,'booktest/pic_upload.html')

# 把图片保存到数据库
def pic_chu(request):
	# FILES.get
	p1 = request.FILES.get('pic')
	pic_obj = PicTest()
	pic_obj.pic = 'booktest/'+p1.name
	pic_obj.save()
	# 保存到本地 数据库保存的是图片地址，一般要重命名
	filename = settings.MEDIA_ROOT+'/booktest/'+p1.name
	with open(filename,'wb') as f:
		# chunks 相当于readlines
		for x in p1.chunks():
			f.write(x)
	return HttpResponse('ok')

# 选择框页面
def area_show(request):
	return render(request, 'booktest/area_show.html')

def area_show2(request):
	# 查找所有省份
	areas = AreaInfo.objects.filter(aParent__isnull=True)
	list1 = [[item.id, item.atitle] for item in areas]
	return JsonResponse({'data':list1})

def area_show3(request, id):
	areas = AreaInfo.objects.filter(aParent_id = id)
	list1 = [[item.id, item.atitle] for item in areas]
	return JsonResponse({'data':list1})

from django.shortcuts import render, redirect
#from comment.models import Comments
from booktest.models import Blog
from comment.forms import CommentForm
# Create your views here.

def comment_blog(request,blog_id):
	blog = Blog.objects.get(id=blog_id)
	if request.method == 'POST':
		# 保存到数据库中
		# 创建一个表单对象，拿到POST请求数据
		form = CommentForm(request.POST)
		# 判断是否符合条件(表单对象的条件)
		if form.is_valid():
			# 不提交，因为还有一个数据blog没有生成，先保存这三个['name', 'email', 'text']
			comment = form.save(commit=False)
			# 添加另一个元素blog，add_time可以自动生成
			comment.blog = blog
			# 提交
			comment.save()

	return redirect('detail',blog_id)
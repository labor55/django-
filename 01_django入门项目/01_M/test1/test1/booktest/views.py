from django.shortcuts import render,redirect
from  django.http import  HttpResponse
from booktest.models import BookInfo, HeroInfo
import random
from datetime import date

# Create your views here.
# get得到一条数据
def book(request,id):
    b1 = BookInfo.objects.get(id=id)
    return HttpResponse(f'{id}:{b1.btitle}')

# 将所有数据传递到index.html文件中，
# 要用切片的方式取出
def index(request):
    books = BookInfo.objects.all()
    context = {'books': books}
    # render 将context参数传给index.html,字典形式
    return render(request,'booktest/index.html',context=context)

# 删除某条数据
def delete(request,id):
    book = BookInfo.objects.get(id=id)
    book.delete()
    return redirect('/index')

# 添加某条数据
def create(request):
    book = BookInfo()
    book.btitle = f'第{random.random()}本书'
    book.bpub_date = date(1991,1,1)
    book.save()
    return redirect('/index')
from django.shortcuts import render,redirect
from booktest.models import HeroInfo,BookInfo,AreaInfo
from django.http import HttpResponse
from datetime import date
# Create your views here.

# 定义首页视图
def index(request):
    books = BookInfo.objects.all()
    dict1 = {'books':books}
    return render(request,'booktest/index.html',context=dict1)

def delete(request,id):
    book = BookInfo.objects.get(id=id)
    book.delete()
    # 跳转到首页
    return redirect('/')

def create(request):
    book = BookInfo()
    book.btitle = '你的名字'
    book.bpub_date = date(1991,1,1)
    book.save()
    # 跳转到首页
    return redirect('/')

# 查询广州市的信息
def area(request):
    area = AreaInfo.objects.get(pk=440100)
    return render(request,'booktest/area.html',{'area':area})

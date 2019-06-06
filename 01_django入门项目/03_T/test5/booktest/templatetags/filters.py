from django.template import Library

# 1.创建一个过滤器
register = Library()

# 2.使用装饰器进行注册
# id 为过滤的对象
@register.filter
def jishu(id, num):
	return id % num



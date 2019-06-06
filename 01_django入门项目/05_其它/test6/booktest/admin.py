from django.contrib import admin
from booktest.models import PicTest, AreaInfo, Blog
# Register your models here.

# 以块的形式显示子对象(一对多对象)
class AreaStackedInline(admin.StackedInline):
	model = AreaInfo  # 关联的子对象
	extra = 2 # 同时额外编辑多少个子类

# 以列表的形式显示子对象（一对多）
class AreaTabularInline(admin.StackedInline):
	model = AreaInfo  # 关联的子对象
	extra = 2 # 同时额外编辑多少个子类


admin.site.register(Blog)
admin.site.register(PicTest)
# admin.site.register(AreaInfo)



@admin.register(AreaInfo)
class AreaAdmin(admin.ModelAdmin):
	# 设置每页显示多少条
	list_per_page = 10

	# 设置操作选项
	# actions_on_top = True  # 默认选项
	actions_on_bottom = True

	# 显示列表，title为类里面的函数
	list_display = ['id','atitle','parent','title']

	# 过滤重复的(字段太多不适用)
	# list_filter = ['atitle']

	# 添加搜索框
	# search_fields = ['aPanent','atitle']
	# 自定义显示顺序，默认的是model中谁先定义谁就先显示
	# fields = ['aPanent','atitle']

	# 分组显示
	fieldsets = (
		('基本', {'fields': ['atitle']}),
		('高级', {'fields': ['aParent']})
		)

	# inlines = [AreaStackedInline]
	inlines = [AreaTabularInline]
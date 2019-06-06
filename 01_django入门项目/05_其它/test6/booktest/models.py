from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

# 定义地区模型类，储存省，市、区县信息
class AreaInfo(models.Model):
	# 标题为后台显示名称
	atitle = models.CharField('标题',max_length=30)
	aParent = models.ForeignKey('self', null=True, blank=True)

	# def parent(self):
	# 	return self.aParent.atitle if self.aParent else ''

	def parent(self):
		if self.aParent is None:
			return ''
		return self.aParent.atitle
	parent.short_description='父级区域名称'

	def title(self):
		return f'{self.atitle}'

	def __str__(self):
		return f'{self.atitle}'
	# 函数方法支持排序
	title.admin_order_field = 'atitle'
	# parent.admin_order_field = 'atitle'

	# 修改方法显示名
	title.short_description = '区域名称'
	parent.short_description = '父级区域名字'

# 图片的模型类

class PicTest(models.Model):
	pic = models.ImageField(upload_to='booktest/')

class Blog(models.Model):
	title = models.CharField(max_length=20)
	read = models.IntegerField(default=0)
	content = models.TextField()
	# 使用富文本编辑器
	# content = UEditorField(width=1000, height=300, toolbars='full')
	def __str__(self):
		return f'{self.title}'
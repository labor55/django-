from django import forms
from comment.models import Comments

class CommentForm(forms.ModelForm):
	'''定义一个表单类'''
	class Meta:
		# 表单和数据库对应
		model = Comments
		fields = ['name', 'email', 'text']
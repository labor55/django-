from django.db import models

# sha1  md5

# Create your models here.
class Account(models.Model):
	"""docstring for Account"""
	name = models.CharField(max_length=20)
	user = models.CharField(max_length=20)
	pwd = models.CharField(max_length=20)
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
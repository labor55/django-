from django.db import models

# Create your models here.
class Comments(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(max_length=64)
	text = models.TextField()
	add_time = models.DateTimeField(auto_now_add=True)
	blog = models.ForeignKey('booktest.Blog')

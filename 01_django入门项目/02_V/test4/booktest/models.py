from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 20)
	read = models.IntegerField(default=0)
	content = models.TextField()

	def __str__(self):
		return self.title

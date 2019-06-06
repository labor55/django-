from django.db import models

# Create your models here.
# 创建模型类，迁移的时候写入数据库
# 创建了一个书类和英雄类，一对多的关系，一本书里面有很多英雄
class BookInfo(models.Model):
    # char类型
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    def __str__(self):
        return f'{self.btitle}'

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return f'{self.hname}'

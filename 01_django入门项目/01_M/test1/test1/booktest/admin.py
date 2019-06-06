from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
# 1 、直接注册（显示）
# # Register your models here.
# admin.site.register(BookInfo)
# admin.site.register(HeroInfo)

# 2、自定义显示面板
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    ordering = ['id']

admin.site.register(BookInfo,BookInfoAdmin)


# 3、官方推荐，使用装饰器
@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcomment']
    ordering = ('-id',)

from django.contrib import admin

# Register your models here.
from login.models import BookInfo, HeroInfo

class HeroInfoStackInline(admin.TabularInline):
    model = HeroInfo  # 要编辑的对象
    extra = 1  # 附加编辑的数量





class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 5  # 这里定义每行显示多少条数据
    # actions_on_bottom = True  操作的属性 如果设置为True 头部和尾部都会显示
    list_display = ["id", "btitle", "pub_date", "hero"]
    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_date']}),
        ('高级', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )
    inlines = [HeroInfoStackInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "hname", "hbook", "read"]
    list_filter = ["hbook", "hgender"]
    search_fields = ["hname"]






admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

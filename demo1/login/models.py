from django.db import models



# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = "图书集"  # 显示的复数名称 主要是为了在admin站点中显示的名字用

    def count(self):
        return len(HeroInfo.objects.filter(hbook__btitle=self.btitle))


    def pub_date(self):
        return self.bpub_date.strftime("%Y年%M月")

    pub_date.short_description = "发布月份"
    pub_date.admin_order_field = "bpub_date"

    def hero(self):
        list1 = []
        for i in self.heroinfo_set.all():
            list1.append(i.hname)
        return "*".join(list1)

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '人物'
        verbose_name_plural = "人物集"

    def read(self):
        return self.hbook.id

    read.short_description = "图书阅读量"
    read.admin_order_field = "hbook"  # 这样就是按照当前那个数值进行排序

    def __str__(self):
        return self.hname

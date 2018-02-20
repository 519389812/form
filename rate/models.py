from django.db import models


class Rate(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name='序号')
    staff = models.CharField(max_length=30, verbose_name='员工')
    star = models.IntegerField(verbose_name='评分')
    time = models.DateTimeField(auto_now=True, verbose_name='提交/修改时间')
    ip_address = models.CharField(max_length=15, verbose_name='IP地址', null=True)

    def __str__(self):
        return '员工：{}   评分：{}   提交时间：{} '.format(self.staff, self.star, self.time)

    class Meta:
        verbose_name = '值机科服务评价'
        verbose_name_plural = '值机科服务评价'

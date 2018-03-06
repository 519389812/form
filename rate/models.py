from django.db import models


class Rate(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    staff = models.CharField(max_length=30, verbose_name='员工')
    service = models.IntegerField(verbose_name='服务水平')
    efficiency = models.IntegerField(verbose_name='办理效率')
    message = models.TextField(max_length=300, verbose_name='留言', null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, verbose_name='提交时间')
    ip_address = models.CharField(max_length=15, verbose_name='IP地址', null=True, blank=True)

    def __str__(self):
        return '员工：{}  评分：{}  服务水平：{}  办理效率：{}    提交时间：{}'.format(
            self.staff, self.service, self.efficiency, self.message, self.time
        )

    class Meta:
        verbose_name = '值机科服务评价'
        verbose_name_plural = '值机科服务评价'

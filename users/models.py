from django.db import models


# Create your models here.
class UserProfile(models.Model):
    USER_GENDER = (
        ('male', '男'),
        ('female', '女'),
    )
    nike_name = models.CharField(max_length=50, verbose_name="昵称", blank=True, default='')
    birthday = models.DateField(verbose_name="生日", blank=True, null=True)
    gender = models.CharField('性别', max_length=6, choices=USER_GENDER, blank=True)
    adress = models.CharField('地址', max_length=100, blank=True)

    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.owner.username

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class UserMailLog(models.Model):
    sendername = models.CharField("Отправитель", max_length=99, default='', blank=False, null=False)
    sendermail = models.EmailField("Адрес отправителя", max_length=155, default='', blank=False, null=False)
    mailtext = models.CharField("Текст письма", max_length=999, default='', blank=False, null=False)
    sendtime = models.DateTimeField("Время отправления", default=timezone.datetime.now, blank=False, null=False)

    def __str__(self):
        return f'от {self.sendermail}'



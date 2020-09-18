from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from allauth.socialaccount.models import SocialAccount, SocialApp

# Create your models here.
from PIL import Image
from io import BytesIO
import requests, os


class CarouselItem(models.Model):
    title = models.CharField("Заголовок", max_length=25, null=False, blank=False, default='ItemHeader')
    description = models.CharField("Описание", max_length=50, null=False, blank=False, default="Base description")
    image = models.ImageField("Картинка" ,default='classic.jpg', null=False, upload_to='carouselfiles')
    delay = models.CharField("Зависание", max_length=3, default='400', null=False)
    active = models.BooleanField(default=True, null=False)

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


    def __str__(self):
        return f'-- {self.title} --'

    def get_active_items():
        return CarouselItem.objects.filter(active=True)

    def save(self):
        super().save()
        with Image.open(self.image.path) as item:
            if item.height > 0 or item.width > 0:
                size = (600, 400)
                im = item.resize(size, Image.ANTIALIAS)
                im.save(self.image.path)


class UserReview(models.Model):
    uploadto = 'socialuser'

    sendername = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Отправитель'
    )
    review = models.TextField("Отзыв", max_length=999, null=False, blank=False)
    create_date = models.DateTimeField("Написан", default=timezone.datetime.now)
    is_moderate = models.BooleanField("Отображать", default=False)
    avatar = models.ImageField("Ава соцсети", default='def.jpg', null=True, blank=True, upload_to=uploadto)


    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    #   FUNCTIONS
    def getUserAvas(self):
        urlpath = ''
        try:
            t = SocialAccount.objects.get(user_id=self.sendername_id) # change to self.sendername_id
            # TODO: add for VK, Facebook, ...
            provideravas = ['picture', 'avatar_url']
            for _ in provideravas:
                if _ in t.extra_data:
                    urlpath = t.extra_data.get(_)
        except ObjectDoesNotExist as e:
            print(e)

        print(urlpath)
        if urlpath:
            try:
                resp = requests.get(urlpath, timeout=4.0)
                print(resp.status_code)
                ext = '.' + resp.headers.get('Content-Type').split('/')[-1]

                filename = self.sendername.username + '(' + timezone.datetime.now().strftime('%d%m%y-%H%M%S') + ')' + ext
                filedir = os.path.join(
                    os.path.dirname(self.avatar.path),
                    self.uploadto,
                )

                filepath = os.path.join(filedir, filename)

                with Image.open(BytesIO(resp.content)) as img:
                    img.save(filepath)
                    self.avatar = os.path.join(self.uploadto, filename)
            except:
                print('!'*50)


    def __str__(self):
        return f"Отзыв от {self.sendername}"


    def save(self):
        self.getUserAvas()
        super().save()
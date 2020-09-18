from django.contrib import admin
from .models import CarouselItem, UserReview
from allauth.socialaccount.models import SocialAccount
# Register your models here.

@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'active')
    list_filter = ('active',)


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ('getReviewStr', 'create_date', 'is_moderate')
    list_filter = ('is_moderate',)
    # readonly_fields = ('sendername', 'review', 'create_date')


    def getReviewStr(self, obj):
        #obj.getUserAvas()
        return obj
    getReviewStr.short_description = "Отзывы"
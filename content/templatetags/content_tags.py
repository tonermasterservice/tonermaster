from django import template
from content.models import CarouselItem, UserReview


register = template.Library()

@register.simple_tag
def showAllActiveCarouselItems():
    return CarouselItem.get_active_items()


@register.simple_tag
def UserReviewText(user):
    try:
        UserReview.objects.get(sendername_id=user.id)
        reviewtext = UserReview.objects.get(sendername_id=user.id)
        return reviewtext.review
    except:
        return False


@register.simple_tag
def showAllModeratedReviews():
    return UserReview.objects.filter(is_moderate=True)
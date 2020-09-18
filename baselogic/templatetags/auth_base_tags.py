from django import template
from allauth.account.forms import LoginForm

register = template.Library()


@register.simple_tag
def loadLoginForm():
    form = LoginForm()
    return form


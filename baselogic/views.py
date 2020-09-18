from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone

# Create your views here.
from baselogic.models import UserMailLog
from content.models import UserReview
from content.forms import ReviewForm
from config.settings import DEFAULT_FROM_EMAIL


class FormHendler(View):
    def post(self, request):
        subject = 'Сообщение от {} c {}'.format(request.POST.get('cf-name', ''), request.POST.get('cf-email', ''))
        message = request.POST.get('cf-message', '')
        from_email = DEFAULT_FROM_EMAIL
        if subject and message and from_email:
            try:
                maillog = UserMailLog()
                maillog.sendername = subject
                maillog.sendermail = request.POST.get('cf-email', '')
                maillog.mailtext = message
                maillog.save()
                # change mail iin list to owner mail
                send_mail(subject, message, from_email, ['yurevich_vital@mail.ru'], fail_silently=False)
            except BadHeaderError:
                messages.add_message(request, messages.INFO, 'Invalid header found.')
                return redirect('/')
            messages.add_message(request, messages.INFO, 'Сообщение отправлено.')
        return HttpResponseRedirect('/')


class SendReviewView(View):
    def post(self, request):
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save(commit=False)
            review.save()
            messages.add_message(request, messages.INFO, 'Ваш отзыв отправлен. Спасибо.')
        else:
            try:
                obj = UserReview.objects.get(sendername_id=request.user.id)
                obj.review = request.POST.get('review')
                obj.is_moderate = False
                obj.create_date = timezone.datetime.now()
                obj.save()
                messages.add_message(request, messages.INFO, 'Ваш отзыв изменен. Спасибо.')
            except:
                print('error')

        return redirect('/')


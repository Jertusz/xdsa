from django_q.tasks import async_task
from api.models import Order
from datetime import datetime, timedelta, time
from django.core.mail import send_mail
from django.utils import timezone


def email_report():
    subject = f'Daily sales report {datetime.now().date()}'
    from_email = 'reports@shop.django'
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_min = datetime.combine(today, time())
    today_max = datetime.combine(tomorrow, time())
    today_min = timezone.make_aware(today_min)
    today_max = timezone.make_aware(today_max)
    html_report = list(map(str, Order.objects.filter(date__range=(today_min, today_max))))
    html_report = '\n'.join(html_report)
    print(html_report)
    to_email = [from_email, 'jedrzej@szadejko.pl']
    send_mail(subject, html_report, from_email, to_email, fail_silently=False)

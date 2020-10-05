from django_q.tasks import async_task
from datetime import datetime
def send_mail(task):
    subject = f'Daily sales report {datetime.now().date()}'
    from_email = 'reports@shop.django'
    to_email = tuple([from_email, 'jedrzej@szadejko.pl'])
    body = str(task.result)
    if task.success:
        async_task('django.core.mail.send_mail',
                subject,
                body,
                from_email,
                to_email
                )

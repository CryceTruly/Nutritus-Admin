from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import os
@receiver(post_save, sender=None)
def food_post_save_receiver(instance, created, *args, **kwargs):
    """
    Handle sending emails to users
    """
    if created:
            try:
                emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
                message = f" Hi, We have added a new food to avoid,Here are the details \n New Food to Avoid: {instance.name} \n Reason:{instance.reason}"
                send_mail(from_email=os.environ.get('EMAIL_HOST_USER','happydennis@gmail.com'),subject='Updates from the nutritius App',message=message, recipient_list=list(emails), fail_silently=False)

            except Exception as identifier:
                    print('proceeding')

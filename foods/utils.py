from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage


class Utils:
    """Utility class that contains helper function"""
    @staticmethod
    def send_email(data):
        """This function sends email to users."""
        EmailMessage(data['subject'],body=data['body'],to=[data['to']]).send(fail_silently=False)
        return

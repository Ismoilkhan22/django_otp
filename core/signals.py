from django.utils import  timezone

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from core.models import OtpToken


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            pass
        else:
            OtpToken.objects.create(user=instance, otp_expires_at=timezone.now()+timezone.timedelta(minutes=5))
            instance.is_active = False
            instance.save()
        # email creadentials
        otp = OtpToken.objects.filter(user=instance).last()
        subject = "Email Verification"
        message = f"""
                    Hi {instance.username}, here is your OTP {otp.otp_code}
                    it is expires in 5 minuts , use the url below to redirect back to the website
                    http://127.0.0.1:8000/verify-email/{instance.username}
                    """
        sender = "ismoilkhan2211@gmail.com"
        receiver = [instance.email,]

        # send email
        send_mail(
            subject,
            message,
            sender,
            receiver,
            fail_silently=False
        )











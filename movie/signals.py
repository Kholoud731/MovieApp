from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from .models import Movie
from django.dispatch import receiver


# deleted for practise onle 
@receiver(post_delete, sender=Movie)
def notify_admin(signal,sender,instance,using,*args, **kwargs):
    send_mail(
    subject="Movie deleted",
    message=f"The movie {instance.name} has been deleted",
    from_email="kholoud.talaat93@gmail.com",
    recipient_list=['kholoud.talaat93@gmail.com'],
    fail_silently=False)


#  lab requirment
@receiver(post_save, sender=Movie)
def my_handler(sender, instance, created, *args, **kwargs):      
    send_mail(
    subject="New Movie Created",
    message=f"new movie {instance.name} has been created",
    from_email="kholoud.talaat93@gmail.com",
    recipient_list=['kholoud.talaat93@gmail.com'],
    fail_silently=False)

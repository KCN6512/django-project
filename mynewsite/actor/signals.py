from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from .models import *

@receiver(post_save, sender=Actor)
def my_handler(created, **kwargs):
    instance = kwargs['instance']
    if created:
        print(f'Пост {instance} создан')
    else:
        print(f'Пост {instance} обновлен')






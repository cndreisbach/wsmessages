from django.db import models
from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel
import channels
from django.dispatch import receiver
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync


class User(AbstractUser):
    pass


class Boop(TimeStampedModel, models.Model):
    sender = models.ForeignKey(to=User,
                               on_delete=models.CASCADE,
                               related_name="sent_boops")
    recipient = models.ForeignKey(to=User,
                                  on_delete=models.CASCADE,
                                  related_name="received_boops")


@receiver(post_save, sender=Boop)
def send_new_boop_message(sender, instance, **kwargs):
    channel_layer = channels.layers.get_channel_layer()
    print("send_new_boop")
    async_to_sync(channel_layer.group_send)(
        f"user-{instance.recipient.pk}", {
            "type": "boop.create",
            "sender": instance.sender.username,
            "recipient": instance.recipient.username
        })

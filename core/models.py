from django.db import models
from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel


class User(AbstractUser):
    pass


class Boop(TimeStampedModel, models.Model):
    sender = models.ForeignKey(to=User,
                               on_delete=models.CASCADE,
                               related_name="sent_boops")
    recipient = models.ForeignKey(to=User,
                                  on_delete=models.CASCADE,
                                  related_name="received_boops")

from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20, verbose_name="User name", blank=False, default='name')
    user_surname = models.CharField(max_length=30, verbose_name="User surname", blank=False, default='surname')
    user_email = models.CharField(max_length=30, verbose_name="User email", blank=False)

    def __str__(self):
        return self.user_name


class ZooEvent(models.Model):
    event_name = models.CharField(max_length=30, verbose_name="Event name", blank=False, default='event')
    event_date = models.DateField(verbose_name="Date", blank=False)
    event_general_count = models.IntegerField(verbose_name="General count", blank=False)

    def __str__(self):
        return self.event_name


class EventsHaveUsers(models.Model):
    tickets_count = models.IntegerField(blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="User")
    zoo_event = models.ForeignKey(ZooEvent, on_delete=models.PROTECT, verbose_name="ZooEvent")

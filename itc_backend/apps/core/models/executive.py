from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from itc_backend.apps.core.models.meta import AbstractTimeStampModel


class SocialMedia(AbstractTimeStampModel):
    """
    Saves social media link and name of the respective social media
    """
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)


class ExecutiveYear(AbstractTimeStampModel):
    """
    Active year of the executive panel
    This model will be used to group particular executive panel based on 'year'
    """
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)


class Executive(AbstractTimeStampModel):
    """
    Detailed executive information,
    Serial will determine the serial index of the executive in the client page
    """
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    executive_year = models.ForeignKey(to=ExecutiveYear, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="executives/", default="default.jpg")
    serial = models.PositiveIntegerField(default=0)
    social_media = models.ManyToManyField(to=SocialMedia, blank=True)


@receiver(sender=Executive, signal=pre_save)
def executive_post_save(sender, instance, *args, **kwargs):
    # Check if previous created object with same executive year
    # has an serial and appoint serial automatically to it
    if instance.serial == 0 and instance.executive_year:
        previous_object = Executive.objects.filter(executive_year=instance.executive_year)
        if previous_object.exists():
            instance.serial = previous_object.latest("id").serial + 1


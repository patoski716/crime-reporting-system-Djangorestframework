from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


# Create your models here.

class Report(models.Model):
    name=models.CharField(max_length=200,null=True)
    title=models.CharField(max_length=500)
    crime_location=models.TextField(blank=True)
    image=models.ImageField(_("Image"), upload_to=upload_to,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



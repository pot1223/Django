from django.db import models
from first.utils import uuid_upload_to

class Item(models.Model):
    name = models.CharField(max_length=100, validators=[])
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo=models.ImageField(blank=True,upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)


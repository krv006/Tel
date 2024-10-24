from django.db import models
from django.db.models import Model, ImageField, CharField, TextField


class Image(Model):
    image = ImageField(upload_to='images/')


class Contact(Model):
    name = CharField(max_length=255)
    phone_number = CharField(max_length=255)
    message = TextField()

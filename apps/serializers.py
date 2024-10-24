from rest_framework import serializers

from apps.models import Contact, Image


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AddModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

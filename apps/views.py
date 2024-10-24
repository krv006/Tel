# views.py
from django.conf import settings
from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from root.settings import DEFAULT_FROM_EMAIL
from .models import Contact, Image
from .serializers import ContactSerializer, AddModelSerializer


@extend_schema(tags=['Contacts'])
class ContactView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        contact = serializer.save()
        name = contact.name
        phone = contact.phone_number
        message = contact.message
        subject = f"Yangi aloqa xabari - {name}"
        email_message = f"Ism: {name}\nTelefon: {phone}\n\nXabar:\n{message}"
        recipient = [DEFAULT_FROM_EMAIL]

        send_mail(
            subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            recipient,
            fail_silently=False,
        )

        return Response({"detail": "Xabaringiz muvaffaqiyatli yuborildi."}, status=status.HTTP_201_CREATED)


@extend_schema(tags=['Add'])
class AddModelCreateApiView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = AddModelSerializer

from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Client, MailDrop, MailRecipient
from .serializers import (ClientSerializer, MailDropSerializer,
                          MailRecipientSerializer)


class ClientViewSet(viewsets.ViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def list(self, request):
        queryset = Client.objects.filter()
        serializer = ClientSerializer(queryset, many=True,
                                      context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Client.objects.filter()
        client = get_object_or_404(queryset, pk=pk)
        serializer = ClientSerializer(client, context={'request': request})
        return Response(serializer.data)


class MailDropViewSet(viewsets.ViewSet):
    serializer_class = MailDropSerializer
    queryset = MailDrop.objects.all()

    def list(self, request, client_pk=None):
        queryset = MailDrop.objects.filter(client=client_pk)
        serializer = MailDropSerializer(queryset, many=True,
                                        context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None, client_pk=None):
        queryset = MailDrop.objects.filter(pk=pk, client=client_pk)
        maildrop = get_object_or_404(queryset, pk=pk)
        serializer = MailDropSerializer(maildrop, context={'request': request})
        return Response(serializer.data)


class MailRecipientViewSet(viewsets.ViewSet):
    serializer_class = MailRecipientSerializer
    queryset = MailRecipient.objects.all()

    def list(self, request, client_pk=None, maildrop_pk=None):
        queryset = MailRecipient.objects.filter(maildrop__client=client_pk,
                                                maildrop=maildrop_pk)
        serializer = MailRecipientSerializer(queryset, many=True,
                                             context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None, client_pk=None, maildrop_pk=None):
        queryset = MailRecipient.objects.filter(pk=pk, maildrop=maildrop_pk,
                                                maildrop__client=client_pk)
        mailrecipient = get_object_or_404(queryset, pk=pk)
        serializer = MailRecipientSerializer(mailrecipient,
                                             context={'request': request})
        return Response(serializer.data)

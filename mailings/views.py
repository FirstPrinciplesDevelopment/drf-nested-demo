from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Client, MailDrop, MailRecipient
from .serializers import (ClientSerializer, MailDropSerializer,
                          MailRecipientSerializer)

# class UserViewSet(viewsets.ViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.

#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """

#     def list(self, request):
#         pass

#     def create(self, request):
#         pass

#     def retrieve(self, request, pk=None):
#         pass

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass


class ClientViewSet(viewsets.ModelViewSet):
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


class MailDropViewSet(viewsets.ModelViewSet):
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

    def create(self, request, *args, **kwargs):
        maildrop = MailDrop()
        maildrop.title = request.POST['title']
        maildrop.client_id = int(self.kwargs['client_pk'])
        maildrop.save()
        serializer = MailDropSerializer(maildrop, context={'request': request})
        return Response(serializer.data)


class MailRecipientViewSet(viewsets.ModelViewSet):
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

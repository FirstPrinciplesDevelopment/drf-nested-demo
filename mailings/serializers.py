from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from .models import Client, MailDrop, MailRecipient


class MailRecipientMailDropSerializer(NestedHyperlinkedModelSerializer):
    """Serialize the relationship from a MailRecipient to a MailDrop."""
    parent_lookup_kwargs = {
        'client_pk': 'client__pk'
    }

    class Meta:
        model = MailDrop
        fields = ('url', 'title')


class MailRecipientSerializer(NestedHyperlinkedModelSerializer):
    """Serialize a MailRecipient object."""
    maildrop = MailRecipientMailDropSerializer(many=False, read_only=True)
    parent_lookup_kwargs = {
        'client_pk': 'maildrop__client__pk', 'maildrop_pk': 'maildrop__pk'
    }

    class Meta:
        model = MailRecipient
        fields = ('id', 'url', 'name', 'maildrop')
        


class MailDropMailRecipientSerializer(NestedHyperlinkedModelSerializer):
    """Serialize the relationship from a MailDrop to many MailRecipients."""
    parent_lookup_kwargs = {
        'client_pk': 'maildrop__client__pk', 'maildrop_pk': 'maildrop__pk'
    }

    class Meta:
        model = MailRecipient
        fields = ('url', 'name')


class MailDropClientSerializer(NestedHyperlinkedModelSerializer):
    """Serialize the relationship from a MailDrop to a Client."""
    parent_lookup_kwargs = {
        'pk': 'pk'
    }
    

    class Meta:
        model = Client
        fields = ('url', 'name',)
        depth = 1



class MailDropSerializer(NestedHyperlinkedModelSerializer):
    """Serialize a MailDrop object."""
    client = MailDropClientSerializer(many=False, read_only=True)
    recipients = MailDropMailRecipientSerializer(many=True, read_only=True)
    parent_lookup_kwargs = {
        'client_pk': 'client__pk'
    }

    class Meta:
        model = MailDrop
        fields = ('id', 'url', 'title', 'client', 'recipients')


class ClientMailDropSerializer(NestedHyperlinkedModelSerializer):
    """Serialize the relationship from a Client to many MailDrops."""
    parent_lookup_kwargs = {
        'client_pk': 'client__pk',
    }

    class Meta:
        model = MailDrop
        fields = ('url', 'title',)


class ClientSerializer(HyperlinkedModelSerializer):
    """Serialize a Client object."""
    maildrops = ClientMailDropSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'url', 'name', 'maildrops',)
        depth = 2

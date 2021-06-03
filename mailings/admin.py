from django.contrib import admin

from .models import Client, MailDrop, MailRecipient

admin.site.register(Client)
admin.site.register(MailDrop)
admin.site.register(MailRecipient)

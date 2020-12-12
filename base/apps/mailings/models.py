from django.db import models


class Client(models.Model):
    """Represents a single client, which can have many mail drops"""
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class MailDrop(models.Model):
    """Represents a client mailing, has one client and many recipients"""
    title = models.CharField(max_length=30, null=False, blank=False)
    client = models.ForeignKey(
        Client, related_name="maildrops", null=False, blank=False,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.title


class MailRecipient(models.Model):
    """Represents a recipient of a mail drop"""
    name = models.CharField(max_length=30, null=False, blank=False)
    maildrop = models.ForeignKey(
        MailDrop, related_name="recipients", null=False, blank=False,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return self.name

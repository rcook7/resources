from django.db.models import Model, CharField
from django.contrib.postgres.fields import ArrayField

class MyLink(Model):
    url = CharField(max_length=100)
    desc = CharField(max_length=1024, blank=True)
    source = CharField(max_length=1024, blank=True)
    owner = CharField(max_length=100, blank=True, null=True)
    tags = ArrayField(CharField(max_length=200), blank=True, null=True)

    def __str__(self):
        return self.url
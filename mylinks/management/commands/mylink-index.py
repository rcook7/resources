from django.core.management.base import BaseCommand, CommandError
from mylinks.search import MyLinkIndex
from mylinks.es_client import es_client

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        MyLinkIndex.init(using=es_client)
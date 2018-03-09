from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .serializers import MyLink, MyLinkElasticSerializer
from .es_client import es_client

@receiver(pre_save, sender=MyLink, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = MyLinkElasticSerializer(instance)
    obj.save(using=es_client)

@receiver(post_delete, sender=MyLink, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = MyLinkElasticSerializer(instance)
    obj.delete(using=es_client, ignore=404)
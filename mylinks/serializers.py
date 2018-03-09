from rest_framework import serializers
from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from .models import MyLink
from .search import MyLinkIndex

class MyLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLink
        fields = ('id', 'url', 'tags', 'desc', 'source', 'owner')

class MyLinkElasticSerializer(ElasticModelSerializer):
    class Meta:
        model = MyLink
        es_model = MyLinkIndex
        fields = ('pk', 'url', 'tags', 'desc', 'source', 'owner')
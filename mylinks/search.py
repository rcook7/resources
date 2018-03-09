from elasticsearch_dsl import DocType, Text, Keyword, Integer
from .es_client import es_client

class MyLinkIndex(DocType):
    pk = Integer()
    url = Text()
    tags = Keyword(multi=True)
    desc = Text()
    source = Text()
    owner = Keyword()

    class Meta:
        index = 'mylink'

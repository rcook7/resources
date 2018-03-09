from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MyLinkViewSet, FilterView

list = {
    'get': 'list',
    'post': 'create'
}
detail = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = format_suffix_patterns([
    url(r'^$', MyLinkViewSet.as_view(list), name='mylink-list'),
    url(r'^(?P<pk>[0-9]+)$', MyLinkViewSet.as_view(detail), name='mylink-detail'),
    url(r'^filter/', FilterView.as_view(), name="mylinks-filter")
])
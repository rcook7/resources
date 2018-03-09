from django.conf.urls import url
from .views import CategoryViewSet, TestViewSet, QuestionViewSet, exams_root
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
category_tests = CategoryViewSet.as_view({
    'get': 'getTests'
}, renderer_classes=[renderers.JSONRenderer, renderers.BrowsableAPIRenderer])


test_list = TestViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
test_detail = TestViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
test_questions = TestViewSet.as_view({
    'get': 'getQuestions'
}, renderer_classes=[renderers.JSONRenderer, renderers.BrowsableAPIRenderer])


question_list = QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', exams_root, name="exams-root"),
    url(r'^categories$', category_list, name='category-list'),
    url(r'^categories/(?P<pk>[0-9]+)/$', category_detail, name='category-detail'),
    url(r'^categories/(?P<pk>[0-9]+)/tests$', category_tests, name='category-tests'),
    url(r'^tests$', test_list, name='test-list'),
    url(r'^tests/(?P<pk>[0-9]+)/$', test_detail, name='test-detail'),
    url(r'^tests/(?P<pk>[0-9]+)/questions$', test_questions, name='test-questions'),
    url(r'^questions$', question_list, name='question-list'),
    url(r'^questions/(?P<pk>[0-9]+)/$', question_detail, name='question-detail'),
])
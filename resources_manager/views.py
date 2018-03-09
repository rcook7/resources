from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'snippets': reverse('snippets-root', request=request, format=format),
        'exams': reverse('exams-root', request=request, format=format),
        'mylinks': reverse('mylink-list', request=request, format=format),
        'schemas': reverse('schemas', request=request, format=format),
    })
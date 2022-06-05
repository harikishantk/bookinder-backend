from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from base.models import *

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/readers'
        'GET /api/readers/id'
    ]
    return Response(routes)

@api_view(['GET'])
def getReaders(request):
    readers = Reader.objects.all()
    serializer = ReaderSerializer(readers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getReader(request, pk):
    readers = Reader.objects.get(id=pk)
    serializer = ReaderSerializer(readers, many=False)
    return Response(serializer.data)
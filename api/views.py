from rest_framework.response import Response
from rest_framework.decorators import api_view
from AppTwo.models import Author
from .serializers import AuthorSerializer

@api_view(['GET'])
def getData(request):
  items = Author.objects.all()
  serializer = AuthorSerializer(items, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def addAuthor(request):
  serializer = AuthorSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response()
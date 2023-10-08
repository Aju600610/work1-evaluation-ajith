#CRUD
from rest_framework.decorators import api_view
from work1App.models import Dictionary
from work1App.serializers import DictionarySerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework import filters


# CRUD
@api_view(['GET'])
def apiOverview(request):
    api_urls = {\
        'Add':'/add/',
        'Search':'/Search_filter/',
        'Update':'/update/<str:pk>',
        'Remove':'/remove/<str:pk>',
        'viewAll':'/viewAll/',
    }
    return Response(api_urls)


class Search_filter(ListAPIView):
    queryset=Dictionary.objects.all()
    serializer_class=DictionarySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['label']

# CREATE
@api_view(['POST'])
def add(request):
    serializer = DictionarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# UPDATE
@api_view(['PUT'])
def update(request,pk):
    rec = Dictionary.objects.get(id=pk) 
    serializer = DictionarySerializer(instance=rec,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#DELETE BY ID
@api_view(['DELETE'])
def remove(request,pk):
    rec = Dictionary.objects.get(id=pk)
    rec.delete()
    return Response("item succesfully deleted")




# READ
@api_view(['GET'])
def viewAll(request):
    tasks = Dictionary.objects.all() #ALL
    serializer = DictionarySerializer(tasks,many=True)
    return Response(serializer.data)







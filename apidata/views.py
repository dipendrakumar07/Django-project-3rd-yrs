from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status   
from .models import ApiData
from .serializers import ApiDataSerializer
@api_view(['GET'])
def api_home(request):
    return Response({"message": "Welcome to ApiData API!"})

@api_view(['GET'])
def get_apidata(request):
    apidata = ApiData.objects.all()
    serializers = ApiDataSerializer(apidata, many=True)
    return Response(serializers.data)    

@api_view(['POST'])
def add_apidata(request):
    serializers = ApiDataSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(
            {"message": "ApiData added!", "data": serializers.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_apidata_item(request, id):
    apidata_item = get_object_or_404(ApiData, id=id)
    serializers = ApiDataSerializer(apidata_item)
    return Response(serializers.data)



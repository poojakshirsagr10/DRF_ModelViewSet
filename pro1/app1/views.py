from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer, Employee
import logging

logger = logging.getLogger('app1')

@api_view(http_method_names=['POST'])
def create_api(request):
    serializer = EmployeeSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET'])
def show_api(request):
    objs=Employee.objects.all()
    serializer = EmployeeSerializer(objs, many=True)
    logger.info('Employee show')
    return Response(data= serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def retrive_api(request,pk):
    obj = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(obj)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=['PUT','PATCH'])
def update_api(request, pk):
    obj = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(data=request.data, instance=obj)
    if serializer.is_valid():
        serializer.save()
        return  Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['DELETE'])
def delete_api(request, pk):
    obj = Employee.objects.get(id=pk)
    obj.delete()
    return Response(data={"msg":"record deleted"})




from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from . import serializers
# Create your views here.

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    '''FIrst api'''
    def get(self,request,format=None):
        '''returns a list of ari view'''
        api_apiview = ['first api']
        return Response({'message':api_apiview})
    
    def post(self,request):
        '''simple post reqest using serializer'''
        seralizer = self.serializer_class(data=request.data)
        if seralizer.is_valid():
            name = seralizer.validated_data.get('name')
            message = {'message':f'hello : {name}'}
            return Response(message)
        else:
            return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None):
        return Response({'message':'put method'})
    
    def patch(self,request,pk=None):
        return Response({'message':'patch'})
    
    def delete(self,reqest,pk=None):
        return Response({'message':'delete'})
    
class HelloViewset(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        a_viewset = [
            '''
            api view set all function tide together 
            create, update, delete, partial_delete
            '''
        ]
        return Response({'message':a_viewset})
    

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello{name}'
            return Response(message)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self,request,pk=None):
        return Response({'message':'get'})
    

    def update(self,request,pk=None):
        return Response({'message':'post'})
    
    def partial_update(self,request,pk=None):
        return Response({'message':'patch'})
    
    def destroy(self,request,pk=None):
        return Response({'message':'delete'})
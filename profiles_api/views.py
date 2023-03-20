from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
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
        if seralizer.is_valid:
            name = seralizer.validated_data.get('name')
            message = {'message':f'hello : {name}'}
            return Response(message)
        else:
            return Response(seralizer.errors,status=status.HTTP_400_BAD_REQUEST)
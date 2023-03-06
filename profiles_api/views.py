from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class HelloApiView(APIView):
    '''FIrst api'''
    def get(self,request,format=None):
        '''returns a list of ari view'''
        return Response({'message':'Hello'})
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    '''new serializers'''
    name = serializers.CharField(max_length = 10)

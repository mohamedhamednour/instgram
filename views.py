from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from demo.models import Post
from rest_framework.views import APIView
from rest_framework.response import Response


from instgram.api import Studentser


class Apostudent(APIView):
    def get(self,requset):
        queryset = Post.objects.all()
        data = Studentser(queryset,many=True).data
        return Response(data)
    def set(self,request):
        silzer = Studentser(data=request.data)
        if silzer.is_valid():
            silzer.save()
            return Response(silzer.data)

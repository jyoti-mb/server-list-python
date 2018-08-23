# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from server_list.serializers import ServerSerializer
from server_list.models import Server
from rest_framework import generics

# Create your views here.
class ServerList(generics.ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
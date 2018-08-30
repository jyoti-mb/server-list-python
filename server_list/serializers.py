from rest_framework import serializers
from server_list.models import Server

class ServerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Server
		fields = ('id', 'url','details', 'created_at','country','city')
from rest_framework import serializers
from server_list.models import Server

class ServerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Server
		fields = ('id', 'name','details', 'created_at')
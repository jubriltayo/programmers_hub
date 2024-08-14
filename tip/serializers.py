from rest_framework import serializers

from .models import Tip



class TipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tip
        fields = ['tipId', 'title', 'description', 'language', 'tags']
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True},
            'language': {'required': True},
        }

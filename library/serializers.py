from rest_framework import serializers
from .models import Bab, Mawdoe, Page

class BabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bab
        fields = ['__all__']
        read_only_fields = ['id']
        
        
class MawdoeSerializer(serializers.ModelSerializer):
    bab = BabSerializer()

    class Meta:
        model = Mawdoe
        fields = '__all__'
        read_only_fields = ['id']


class PageSerializer(serializers.ModelSerializer):
    mawdoe = MawdoeSerializer()

    class Meta:
        model = Page
        fields = '__all__'
        read_only_fields = ['id']
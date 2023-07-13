from rest_framework.serializers import ModelSerializer

from my_dreams.models import Dream


class DreamSerializer(ModelSerializer):
    class Meta:
        model = Dream
        fields = ['name', 'description', 'wish_rate']

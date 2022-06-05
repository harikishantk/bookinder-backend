from rest_framework.serializers import ModelSerializer
from base.models import Reader

class ReaderSerializer(ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'
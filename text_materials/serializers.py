from rest_framework.serializers import ModelSerializer
from files.serializers import HeaderImageSerializer
from .models import Article


class ArticlePreviewSerializer(ModelSerializer):
    header_image = HeaderImageSerializer()

    class Meta:
        model = Article
        fields = '__all__'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    status,
    permissions
)
from . import serializers
from . import models


class GetArticlesPreview(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        queryset = models.Article.objects.slider_preview()
        serializer = serializers.ArticlePreviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

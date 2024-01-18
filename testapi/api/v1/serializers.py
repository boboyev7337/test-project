from rest_framework import serializers

from testapi.api.v1.exceptions import ImageException
from testapi.models import Test, Category, Post


class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('name', 'smth')


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate_image(self, image):
        max_size = 1.0
        print(image.name)
        if image.size > max_size*1024*1024:
            raise ImageException()


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'description')

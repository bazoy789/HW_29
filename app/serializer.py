from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from app.models import Ad, Category
from users.models import User


class SerializerAd(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class SerializerAdList(serializers.ModelSerializer):
    author_id = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category_id = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


# class SerializerAdDetail(serializers.ModelSerializer):
#     author = SerializerDetailUser()
#     category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())
#
#     class Meta:
#         model = Ad
#         fields = "__all__"

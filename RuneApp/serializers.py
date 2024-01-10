from rest_framework import serializers
from RuneApp.models import Category, Characteristic, Rune


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class RuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rune
        fields = '__all__'

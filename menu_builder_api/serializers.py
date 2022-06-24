from rest_framework import serializers
from .models import Section, Items, Modifiers


class SectionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)

    class Meta:
        model = Section
        fields = ('__all__')


class ItemsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    price = serializers.FloatField()

    class Meta:
        model = Items
        fields = ('__all__')


class ModifiersSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=200)
    items = ItemsSerializer(read_only=True, many=True)

    class Meta:
        model = Modifiers
        fields = ('items', 'description',)


class SectionItemsSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many=True, read_only=True)
    items = ItemsSerializer(many=True, read_only=True)
    modifiers = ModifiersSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['section', 'items', 'modifiers']






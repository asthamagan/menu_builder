from rest_framework import serializers
from .models import Menu, Items, Modifiers


class MenuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)

    class Meta:
        model = Menu
        fields = ('__all__')


class ItemsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)

    class Meta:
        model = Items
        fields = ('__all__')


class ModifiersSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)

    class Meta:
        model = Modifiers
        fields = ('__all__')


class MenuItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    menu = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Items
        fields = ['title', 'menu']


class ModifiersItemsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Modifiers
        fields = ['title', 'items']


class MenuItemsSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many=True, read_only=True)
    items = MenuItemSerializer(many=True, read_only=True)
    modifiers = ModifiersItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ['menu', 'items', 'modifiers']





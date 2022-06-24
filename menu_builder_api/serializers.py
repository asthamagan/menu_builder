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
        extra_kwargs = {'modifiers': {'required': False}}


class ModifiersSerializer(serializers.ModelSerializer):
    modifiers_description = serializers.CharField(max_length=200)
    items = ItemsSerializer(read_only=True, many=True)

    class Meta:
        model = Modifiers
        fields = ('items', 'modifiers_description',)
        extra_kwargs = {'items': {'required': False}}


class ItemsModifiersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    modifier_item = ModifiersSerializer(many=True, read_only=True)

    class Meta:
        model = Items
        fields = ('name', 'description', 'price', 'modifier_item',)


class SectionItemsSerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['name', 'description', 'items']




# mapping of Items and Modifiers
class ModifierItemsMapSerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True)

    def get_or_create_items(self, items):
        items_ids = []
        for item in items:
            item_instance, created = Items.objects.get_or_create(pk=item.get('id'), defaults=item)
            items_ids.append(item_instance.pk)
        return items_ids

    def create_or_update_items(self, items):
        items_ids = []
        for item in items:
            item_instance, created = Items.objects.update_or_create(pk=item.get('id'), defaults=item)
            items_ids.append(item_instance.pk)
        return items_ids

    def create(self, validated_data):
        items = validated_data.pop('items', [])
        modifier = Modifiers.objects.create(**validated_data)
        modifier.items.set(self.get_or_create_items(items))
        return modifier

    def update(self, instance, validated_data):
        items = validated_data.pop('items', [])
        instance.items.set(self.create_or_update_items(items))
        fields = ['modifiers_description']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:  # validated_data may not contain all fields during HTTP PATCH
                pass
        instance.save()
        return instance

    class Meta:
        model = Modifiers
        fields = "__all__"





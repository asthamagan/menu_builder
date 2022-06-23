from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import (
    MenuSerializer,
    ItemsSerializer,
    ModifiersSerializer,
    MenuItemsSerializer
)
from .models import Menu, Items, Modifiers
from django.shortcuts import get_object_or_404


# Create your views here.
class MenuViews(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Menu.objects.get(id=id)
            serializer = MenuSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Menu.objects.get(id=id)
        serializer = MenuSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Menu, id=id)
        item.delete()
        return Response({"status": "success", "data": "Menu Deleted"})


class ItemsViews(APIView):
    def post(self, request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Items.objects.get(id=id)
            serializer = ItemsSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Items.objects.get(id=id)
        serializer = ItemsSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Menu, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class ModifiersViews(APIView):
    def post(self, request):
        serializer = ModifiersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Modifiers.objects.get(id=id)
            serializer = ModifiersSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Modifiers.objects.all()
        serializer = ModifiersSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Modifiers.objects.get(id=id)
        serializer = ModifiersSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Menu, id=id)
        item.delete()
        return Response({"status": "success", "data": "Modifier Deleted"})


class ModifierItemsMenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuItemsSerializer
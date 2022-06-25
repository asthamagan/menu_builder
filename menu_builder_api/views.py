from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.http import JsonResponse
from .serializers import (
    SectionSerializer,
    ItemsSerializer,
    ModifiersSerializer,
    SectionItemsSerializer,
    ModifierItemsMapSerializer,
    MenulistSerializer
)
from .models import Section, Items, Modifiers
from django.shortcuts import get_object_or_404


# Create your views here.
class MenuViews(APIView):
    def post(self, request):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Section.objects.get(id=id)
            serializer = SectionSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Section.objects.all()
        serializer = SectionSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Section.objects.get(id=id)
        serializer = SectionSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Section, id=id)
        item.delete()
        return Response({"status": "success", "data": "Section Deleted"})


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
        item = get_object_or_404(Section, id=id)
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
        item = get_object_or_404(Modifiers, id=id)
        item.delete()
        return Response({"status": "success", "data": "Modifier Deleted"})


class ModifierItemsMenuViewSet(APIView):

    def get(self, request, **kwargs):
        queryset = Section.objects.all()
        serializer_class = MenulistSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer_class.data}, status=status.HTTP_200_OK)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = ModifierItemsMapSerializer
    queryset = Modifiers.objects.all()

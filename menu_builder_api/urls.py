from django.urls import path
from .views import MenuViews, ItemsViews, ModifiersViews, ModifierItemsMenuViewSet

urlpatterns = [
    path('menu/', MenuViews.as_view()),
    path('menu/<int:id>', MenuViews.as_view()),
    path('items/', ItemsViews.as_view()),
    path('items/<int:id>', ItemsViews.as_view()),
    path('modifiers/', ModifiersViews.as_view()),
    path('modifiers/<int:id>', ModifiersViews.as_view()),
    path('menu_data', ModifierItemsMenuViewSet.as_view({'get': 'list'})),
]
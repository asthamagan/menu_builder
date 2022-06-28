from django.urls import path, include
from .views import (
    MenuViews,
    ItemsViews,
    ModifiersViews,
    ModifierItemsMenuViewSet,
    OrderViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items-modifiers', OrderViewSet, basename='items-modifiers')
# app_name = 'menu_builder_api'
urlpatterns = [
    path('', include(router.urls)),
    path('section/', MenuViews.as_view(), name='section'),
    path('section/<int:id>', MenuViews.as_view(), name='section_id'),
    path('items/', ItemsViews.as_view(), name='items'),
    path('items/<int:id>', ItemsViews.as_view(), name='item_id'),
    path('modifiers/', ModifiersViews.as_view(), name='modifier'),
    path('modifiers/<int:id>', ModifiersViews.as_view(), name='modifier_id'),
    path('section_data/', ModifierItemsMenuViewSet.as_view(), name='section_data'),
    # path('items-modifiers/', ItemsModifiersViewSet.as_view()),

]
urlpatterns += router.urls
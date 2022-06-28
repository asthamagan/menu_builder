from django.urls import path
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

urlpatterns = [
    path('section/', MenuViews.as_view(), name='section'),
    path('section/<int:id>', MenuViews.as_view()),
    path('items/', ItemsViews.as_view()),
    path('items/<int:id>', ItemsViews.as_view()),
    path('modifiers/', ModifiersViews.as_view()),
    path('modifiers/<int:id>', ModifiersViews.as_view()),
    path('section_data/', ModifierItemsMenuViewSet.as_view()),
    # path('items-modifiers/', ItemsModifiersViewSet.as_view()),

]
urlpatterns += router.urls
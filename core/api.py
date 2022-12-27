from django.urls import path
from core.views import *


urlpatterns = [
    path('category/',
         CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('category/<int:pk>',
         CategoryViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('subcategory/',
         SubCategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('subcategory/<int:pk>',
         SubCategoryViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    
]

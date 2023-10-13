from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.InventoryListView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', views.InventoryDetailView.as_view(), name='inventory-detail'),
    path('brand/', views.BrandListView.as_view(), name='brand-list'),
    path('brand/<int:pk>/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('room/', views.RoomListView.as_view(), name='room-list'),
    path('room/<int:pk>/', views.RoomDetailView.as_view(), name='room-detail'),
]

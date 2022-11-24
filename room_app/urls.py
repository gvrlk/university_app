from django.urls import path, include
from .views import RoomListView, RoomDetailView


urlpatterns = [
    path('', RoomListView.as_view(), name='room-list'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
]
from django.urls import path
from . import views
urlpatterns = [
    path('restaurant-list/', views.RestaurantCreateView.as_view(), name='restaurant-list'),
    path('restaurant-detail/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('users/', views.UserListView.as_view(), name='user-list'),
]

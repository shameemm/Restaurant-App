from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('register/',views.UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
    path('add_bookmark/', views.BookmarkView.as_view(), name='add_bookmark'),
    path('user_bookmark/<int:pk>/', views.UserBookmarksView.as_view(), name='user_bookmark'),
    path('review/', views.ReviewRatingView.as_view(),name="review"),
    path('review/<int:pk>/', views.ReviewRatingView.as_view(),name="review"),
    path('filter/', views.FilterRestaurant.as_view(), name='filter'),
]

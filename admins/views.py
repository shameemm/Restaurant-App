from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Restaurant
from rest_framework import status
from django.contrib.auth.models import User
from .permissions import IsAdminUser
from .serializers import RestaurantSerializer

# Create your views here.
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class RestaurantCreateView(APIView, CustomPagination):
    permission_classes = [IsAdminUser]
    def get(self, request):
        restaurants = Restaurant.objects.all()
        
        paginated_restaurants = self.paginate_queryset(restaurants, request)
        if paginated_restaurants is not None:
            serializer = RestaurantSerializer(paginated_restaurants, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetailView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            restaurant.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
class UserListView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        users = User.objects.all()
        user_data = [{'id': user.id, 'username': user.username, 'is_active': user.is_active} for user in users]
        return Response(user_data)
    
    def post(self, request):
        user_id = request.data.get('user_id')
        action = request.data.get('action')
        
        if not user_id or action not in ['activate','deactivate']:
            return Response({'mesaage':'Invalid Request'}, status = status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if action == 'activate':
            user.is_active =True
            action_msg = 'activated'
        elif action=='deactivate':
            user.is_active = False
            action_msg = 'deactivated'
            
        user.save()
        return Response({'message':f'User {user.username} has been {action_msg}'})
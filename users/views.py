from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, BookmarkSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from admins.permissions import IsRegularUser
from django.db.models import Avg
from admins.views import CustomPagination
from admins.models import Restaurant
from .models import Bookmark, Review
from admins.serializers import RestaurantSerializer

# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class RestaurantView(APIView, CustomPagination):
    permission_classes = [IsRegularUser]
    def get(self, request):
        restaurants = Restaurant.objects.all()
        
        paginated_restaurants = self.paginate_queryset(restaurants, request)
        if paginated_restaurants is not None:
            serializer = RestaurantSerializer(paginated_restaurants, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
class BookmarkView(APIView):
    permission_classes = [IsRegularUser]
    def post(self, request):
        serializer = BookmarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserBookmarksView(APIView):
    permission_classes = [IsRegularUser]
    def get_object(self,pk):
        try:
            return Bookmark.objects.get(user_id=pk)
        except Restaurant.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    #get bookmark related with current user
    def get(self, request, pk):
        bookmark = self.get_object(pk)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data)
    
class ReviewRatingView(APIView):
    permission_classes = [IsRegularUser]
    def post(self,request):
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            restaurant = request.data.get('restaurant')
            reviews_count = Review.objects.filter(restaurant=restaurant).count()
            avg_rating = Review.objects.filter(restaurant=restaurant).aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
            
            Restaurant.objects.filter(id=restaurant).update(rating=avg_rating)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self,pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
class FilterRestaurant(APIView):
    permission_classes = [IsRegularUser]
    def get(self, request):
            min_rating = request.query_params.get('min_rating', 3.5)
            search_query = request.query_params.get('search', '')
            restaurants = Restaurant.objects.filter(rating__gte=min_rating)

            if search_query:
                restaurants = restaurants.filter(name__icontains=search_query)
            
            serializer = RestaurantSerializer(restaurants, many=True)
            return Response(serializer.data)
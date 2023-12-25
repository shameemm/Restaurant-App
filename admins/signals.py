from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import Restaurant
from users.models import Review

@receiver([post_save, post_delete], sender=Review)
def update_restaurant_rating(sender, instance, **kwargs):
    restaurant = instance.restaurant
    avg_rating = Review.objects.filter(restaurant=restaurant).aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
    
    # Get the restaurant instance
    restaurant_instance = Restaurant.objects.filter(id=restaurant.id).first()

    if restaurant_instance:
        restaurant_instance.rating = avg_rating
        restaurant_instance.save()
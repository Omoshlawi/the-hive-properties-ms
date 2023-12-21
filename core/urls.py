from rest_framework import routers
from django.urls import path
from properties import views as property_view
from groups import views as group_view
from listings import views as listing_view
from . import views


urlpatterns = [
    path("", views.RootView.as_view())
]

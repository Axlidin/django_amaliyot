from django.urls import path
from .views import HomeView, MessageCreateView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('', MessageCreateView.as_view(), name='create_message'),
]

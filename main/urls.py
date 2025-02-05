from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/edit/', EditView.as_view()),
    path('<int:pk>/delete/', DeleteView.as_view()),
]

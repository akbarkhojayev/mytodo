from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import token_obtain_pair , token_refresh
from main.views import *
from django.urls import path

schema_view = get_schema_view(
  openapi.Info(
     title="Snippets API",
     default_version='v1',
     description="Test description",
     terms_of_service="https://www.google.com/policies/terms/",
     contact=openapi.Contact(email="contact@snippets.local"),
     license=openapi.License(name="BSD License"),
  ),
  public=True,
  permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('token/', token_obtain_pair ),
    path('token/refresh/', token_refresh ),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns += [
    path('todos/', TaskListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TaskDetailView.as_view(), name='todo-detail'),
    path('todo/add/' , TaskCreateView.as_view(), name='todo-add')
]
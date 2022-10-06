from django.urls import path

from .views import *

urlpatterns = [
    path('order/list/', OrderView.as_view()),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view()),

    path('product/list/', ProductView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path("swagger/main", schema_view.with_ui("swagger", cache_timeout=0)),
    path("swagger/yaml", schema_view.without_ui(cache_timeout=0)),
    path("swagger/json", schema_view.without_ui(cache_timeout=0)),


]
from django.urls import path

from .views import OrderView

urlpatterns = [
    path('order/list', OrderView.as_view()),
]
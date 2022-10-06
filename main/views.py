import django_filters
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi as drf_yasg_openapi
from drf_yasg import views as drf_yasg_views
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

schema_view = drf_yasg_views.get_schema_view(
    drf_yasg_openapi.Info(
        title="Education  API",
        default_version="v1",
        # description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=drf_yasg_openapi.Contact(url="https://t.me/abbos_software"),
        license=drf_yasg_openapi.License(name="Proprietary software license"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny, ),
)


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['order', "id", "price", "product_id"]
    pagination_class = ProductPagination


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

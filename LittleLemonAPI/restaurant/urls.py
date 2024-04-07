#define URL route for index() view
from django.urls import path
from .views import index, home, MenuItemView, SingleMenuItemView, BookingViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single_menu_item'),
    path('api-token-auth/', obtain_auth_token)
]

# Include router.urls for booking-related endpoints
urlpatterns += router.urls
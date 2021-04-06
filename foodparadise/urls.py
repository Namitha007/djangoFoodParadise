from django.urls import include, path
from rest_framework import routers
from . import views
from .models import Contact, Reservation, Menu

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('contact/', views.ContactList.as_view()),
    path('contact_details/<int:pk>/', views.ContactDetail.as_view()),

    path('reservation/', views.ReservationList.as_view()),
    path('reservation_details/<int:pk>/', views.ReservationDetail.as_view()),

    path('menu/', views.MenuList.as_view()),
    path('menu_details/<int:pk>/', views.MenuDetail.as_view()),

]
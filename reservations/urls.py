from django.urls import path
from .views import RoomList, BookingList, BookingView
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.home, name='landing-page'),
    path('about', views.about, name='about-page'),
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view'),
]
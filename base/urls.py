from django.urls import path
from . import views

urlpatterns = [
  path('login/',views.loginPage,name="login"),
  path('logout/',views.logoutPage,name="logout"),
  path('',views.home,name="home"),
  path('room/<str:pk>/',views.room,name="room"),
  path('room-form/',views.room_form,name="room_form"),
  path('update-form/<str:pk>/',views.updateRoom,name='update-form'),
  path('delete-form/<str:pk>/',views.deleteRoom,name='delete-form')
]
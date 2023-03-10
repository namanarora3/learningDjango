from django.urls import path
from . import views

urlpatterns = [
  path('login/',views.loginPage,name="login"),
  path('register/',views.registerPage,name="register"),
  path('logout/',views.logoutPage,name="logout"),
  path('',views.home,name="home"),
  path('room/<str:pk>/',views.room,name="room"),
  path('user-profile/<str:pk>/',views.user_profile,name="user-profile"),
  path('room-form/',views.room_form,name="room_form"),
  path('update-form/<str:pk>/',views.updateRoom,name='update-form'),
  path('delete-form/<str:pk>/',views.deleteRoom,name='delete-form'),
  path('delete-message/<str:pk>/',views.delete_message,name='delete-message')
]
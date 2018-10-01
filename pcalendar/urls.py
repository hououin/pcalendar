from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('', views.index, name='home' ),

    path('calendar',views.calendar, name="calendar"),

    path('showtasks', views.showtasks, name='tasks'),
]

from django.urls import path

from spotify import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('music/<int:pk>', views.music, name='music')
]

from django.urls import path

from spotify import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('music/<int:pk>', views.music, name='music'),
    path('some/', views.afternext, name='afternext'),
    path('random/', views.randommusic, name="randommusic"),
    path('addmusic/', views.MusicAdd, name="addmusicy"),
    path('add_to_favorite/<int:pk>/', views.add_to_favorite, name='add_to_favorite'),
    path('favorite/', views.favorite, name="favorite"),

]

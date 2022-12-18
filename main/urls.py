from django.urls import path
from . import views

urlpatterns=[
    path('', views.Main, name='home' ),
    path('<int:id>', views.film_details, name='film_details' ),
    path('film_create/', views.film_create,name='film_create'),
    path('search/', views.search, name='search'),
    path('category/<int:id>/', views.category, name='category'),
    path('del/<int:id>', views.film_delate, name='del' )
]
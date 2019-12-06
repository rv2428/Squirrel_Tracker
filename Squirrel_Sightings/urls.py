from django.urls import path

from . import views

urlpatterns = [ 
        path('',views.index),
        path('map/',views.coordinates),
        path('<str:Unique_Squirrel_Id>/', views.edit_squirrel),
]

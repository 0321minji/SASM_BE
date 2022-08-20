from .views import PlaceDetailView, place_like, save_place_db
from django.urls import path

urlpatterns =[
    path('place_like/<int:id>/', place_like, name="place_like"),
    path('save_place/', save_place_db),
    path('place_detail/<int:pk>/',PlaceDetailView.as_view({'get': 'get'}),name="place_detail"),
    path('place_list/',PlaceDetailView.as_view({'get':'list'}), name='place_list')
]

from django.urls import path, include
from cars.views import CarsListView, CarDetailView, CarAdd


urlpatterns = [
    path('', CarsListView.as_view(), name='main'),
    path('add', CarAdd.as_view(), name='add'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]

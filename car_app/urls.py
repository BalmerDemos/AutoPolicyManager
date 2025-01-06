from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("cars", views.cars_view, name="cars-page"),
    path('car-detail/<int:pk>/',     views.car_detail_view, name='car-detail'),
    path('update-deatils/<int:pk>/', views.update_detail_view, name='update-details'),
    path("update-success/<int:pk>/", views.update_success_view, name="update-success"),
    path("delete-car/<int:pk>/", views.delete_car_view, name="delete-car"),
    path("delete-success/<int:pk>/", views.delete_success_view, name="delete-success"),
    path("contact", views.ContactPageView.as_view(), name="contact-page"),
]


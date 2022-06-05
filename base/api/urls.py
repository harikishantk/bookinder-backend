from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('readers', views.getReaders),
    path('readers/<int:pk>', views.getReader)
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('aboutus/', views.about_us_view, name='aboutus'),
    path('callus/', views.call_us_view, name='callus'),
]

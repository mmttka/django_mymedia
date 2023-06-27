from django.urls import path

from . import views

urlpatterns = [
    path('tech/', views.ListTechView.as_view(), name='list-tech'),
    path('tech/<int:pk>/detail/', views.DetailTechView.as_view(),name='detail-tech'),
    path('tech/<int:pk>/delete/', views.DeleteTechView.as_view(),name='delete-tech'),
    path('tech/<int:pk>/update/', views.UpdateTechView.as_view(),name='update-tech'),
    path('add_form', views.add_form, name='add_form'),
]
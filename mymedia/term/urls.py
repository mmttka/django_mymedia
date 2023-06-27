from django.urls import path

from . import views

urlpatterns = [
    path('term/', views.ListTermView.as_view(), name='list-term'),
    path('term/<int:pk>/detail/', views.DetailTermView.as_view(),name='detail-term'),
]
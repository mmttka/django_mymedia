from django.urls import path

from . import views

urlpatterns = [
    path('topic/', views.ListTopicView.as_view(), name='list-topic'),
    path('topic/<int:pk>/detail/', views.DetailTopicView.as_view(),name='detail-topic'),
]

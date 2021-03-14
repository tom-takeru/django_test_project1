from django.urls import path

from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.MemoListView.as_view(), name='memo_list'),
    path('memo_create/', views.MemoCreateView.as_view(), name='memo_create'),
]
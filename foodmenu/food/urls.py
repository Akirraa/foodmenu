from django.urls import path 
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.indexClassView.as_view(), name='index'),
    path('<int:pk>/', views.detailClassView.as_view(), name='detail'),
    path('add-item/', views.createClassView.as_view(), name='form'),  
    path('edit/<int:item_id>/', views.edit, name='edit'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path( '', views.retrieve_data, name='retrieve_data'),
    path( 'a/', views.retrieve_data, name='retrieve_data'),
    path('upload/', views.upload_data, name='upload_data'),
    path('view/<int:pk>/', views.view_data, name='view_data'),
    path('update/<int:pk>/', views.update_data, name='update_data'),
    path('delete/<int:pk>/', views.delete_data, name='delete_data'),
    
]

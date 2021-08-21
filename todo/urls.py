from django.urls import path
from todo import views

urlpatterns = [
    path('', views.get_routes),
    path('notes/', views.get_notes),
    path('notes/create/', views.create_note),
    path('note/<pk>/update/', views.update_note),
    path('note/<pk>/delete/', views.delete_note),
    path('note/<pk>', views.get_note),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.redireccionar_a_login, name='redireccionar_a_login'),
    path('login/', views.login, name='login'),
    path('tareas/', views.inicio, name='inicio'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('detalle/<int:id>/', views.detalle_tarea, name='detalle_tarea'),
    path('editar/<int:id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:id>', views.eliminar_tarea, name='eliminar_tarea'),

    # API
    path('api/login/', views.LoginAPIView.as_view(), name='login_api'),
    path('api/tareas/', views.TareasAPIView.as_view(), name='tareas_api'),
]
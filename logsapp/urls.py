from django.urls import path
from .views import logs_graph,logs_list_view

urlpatterns = [
    path('graph/', logs_graph, name='logs_graph'),
    path('list/', logs_list_view, name='logs-list'),
]

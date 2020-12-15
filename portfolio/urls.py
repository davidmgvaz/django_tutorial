from django.urls import path

from .views import ProjetoList, comentar

urlpatterns = [
    path('', ProjetoList.as_view(), name='projetos'),
    path('<int:pk>', comentar, name='projeto'),
]

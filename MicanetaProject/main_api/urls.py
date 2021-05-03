from django.urls import path
from .views import EquipoList, EquipoDetail

app_name = 'main_api'

urlpatterns = [
    path('<int:pk>/', EquipoDetail.as_view(), name='detailcreate'),
    path('', EquipoList.as_view(), name='listcreate'),
]

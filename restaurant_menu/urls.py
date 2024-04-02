from django.urls import path, reverse
from . import views


urlpatterns = [
    path('', views.MenuList.as_view(), name='index'),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item')
]

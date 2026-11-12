
from django.urls import path
from farm import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),

    # Crops
    path('list_crops/', views.crop_list_view, name='my_crops'),
    path('add_crops/', views.crop_create_view, name='crop_create'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('edit_crops/<int:pk>/', views.crop_update_view, name='crop_update'),
    path('delete_crops/<int:pk>/', views.crop_delete_view, name='crop_delete'),
    path('detail_crops/<int:pk>/', views.crop_detail_view, name='crop_detail'),
    path('crops_expenses/<int:pk>/', views.expense_create_view, name='expense_create'),
    path('crops_sales/<int:pk>/', views.sale_create_view, name='sale_create'),
    ]



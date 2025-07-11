from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),  # Changed: signup is now the root/first page
    path('login/', views.login_view, name='login'),  # Added: login now has its own path
    path('setup/', views.setup_view, name='setup'),
    path('preview/', views.preview_view, name='preview'),
    path('delete/<int:contact_id>/', views.delete_account, name='delete_account'),
    path('update/<int:pk>/', views.update_account, name='update_account'),
    path('home/', views.home_view, name='home'),  
    path('download/accounts/', views.download_accounts_csv, name='download_accounts_csv'),
    path('download/request/', views.request_download, name='request_download'),
    path('download/approve/<uuid:token>/', views.approve_download, name='approve_download'),
    path('download/reject/<uuid:token>/', views.reject_download, name='reject_download'),
    path('delete_all/', views.delete_all_accounts, name='delete_all_accounts'),
    path('delete/<int:contact_id>/', views.delete_account, name='delete_account'),
    path('delete-all/', views.delete_all_accounts, name='delete_all_accounts'),
]
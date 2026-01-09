from django.urls import path
from . import views

urlpatterns = [
    # Home and authentication
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
    path('dashboard/photographer/', views.photographer_dashboard, name='photographer_dashboard'),

    # Packages
    path('packages/', views.packages_list, name='packages_list'),
    path('packages/<int:pk>/', views.package_detail, name='package_detail'),

    # Bookings
    path('booking/create/', views.create_booking, name='create_booking'),
    path('booking/create/<int:package_id>/', views.create_booking, name='create_booking_with_package'),
    path('booking/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('booking/<int:booking_id>/comment/', views.add_comment, name='add_comment'),
    path('booking/<int:booking_id>/assign/', views.assign_photographer, name='assign_photographer'),

    # Photos
    path('booking/<int:booking_id>/upload/', views.upload_photos, name='upload_photos'),
    path('booking/<int:booking_id>/gallery/', views.gallery_view, name='gallery'),
    path('photo/<int:photo_id>/select/', views.select_photo, name='select_photo'),
    path('photo/<int:photo_id>/download/', views.download_photo, name='download_photo'),

    # Workflow
    path('workflow/<int:stage_id>/update/', views.update_workflow, name='update_workflow'),

    # Profile
    path('profile/', views.profile_view, name='profile'),
]

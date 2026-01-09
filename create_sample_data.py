#!/usr/bin/env python
"""Create sample data for the photography studio"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photography_studio.settings')
django.setup()

from studio.models import Package
from django.contrib.auth.models import User

# Create sample packages
packages = [
    {
        'name': 'Wedding Basic',
        'description': 'Perfect starter package for intimate wedding ceremonies. Includes essential coverage of your special day.',
        'price': 500,
        'duration_hours': 4,
        'number_of_photos': 100,
        'features': '''Professional photographer for 4 hours
100 edited high-resolution photos
Online gallery for viewing and downloading
Basic photo retouching
1 hour pre-wedding consultation''',
        'is_active': True,
    },
    {
        'name': 'Wedding Premium',
        'description': 'Our most popular wedding package with comprehensive coverage and premium editing.',
        'price': 1200,
        'duration_hours': 8,
        'number_of_photos': 300,
        'features': '''Professional photographer for 8 hours
300 edited high-resolution photos
Premium photo retouching
Online gallery with download options
Engagement session included
Same day sneak peek photos
USB drive with all photos
2 hour pre-wedding consultation''',
        'is_active': True,
    },
    {
        'name': 'Portrait Session',
        'description': 'Professional portrait photography for individuals, couples, or families.',
        'price': 200,
        'duration_hours': 2,
        'number_of_photos': 30,
        'features': '''2 hour photo session
30 professionally edited photos
Choice of indoor or outdoor location
Outfit changes welcome
Online gallery access
Print-ready high-resolution files''',
        'is_active': True,
    },
    {
        'name': 'Corporate Event',
        'description': 'Professional coverage for your business events, conferences, and corporate gatherings.',
        'price': 800,
        'duration_hours': 6,
        'number_of_photos': 200,
        'features': '''6 hours of event coverage
200+ edited photos
Candid and posed shots
Group photos and headshots
Fast 48-hour delivery
Commercial usage rights included
Online gallery for easy sharing''',
        'is_active': True,
    },
    {
        'name': 'Birthday Party',
        'description': 'Capture the joy and memories of your special birthday celebration.',
        'price': 300,
        'duration_hours': 3,
        'number_of_photos': 75,
        'features': '''3 hours of party coverage
75 edited photos
Candid moments and group shots
Cake cutting ceremony coverage
Online gallery
Quick 72-hour delivery''',
        'is_active': True,
    },
]

print("Creating sample packages...")
for pkg_data in packages:
    pkg, created = Package.objects.get_or_create(
        name=pkg_data['name'],
        defaults=pkg_data
    )
    if created:
        print(f"✓ Created: {pkg.name}")
    else:
        print(f"- Already exists: {pkg.name}")

# Update admin user profile to photographer
try:
    admin_user = User.objects.get(username='admin')
    admin_user.first_name = 'Admin'
    admin_user.last_name = 'Photographer'
    admin_user.save()

    profile = admin_user.profile
    profile.user_type = 'photographer'
    profile.phone = '+1234567890'
    profile.address = '123 Photography Studio, City, State'
    profile.save()
    print(f"\n✓ Updated admin profile to photographer")
except Exception as e:
    print(f"\nNote: {e}")

print("\n" + "="*50)
print("Sample data created successfully!")
print("="*50)
print("\nLogin credentials:")
print("  Username: admin")
print("  Password: admin123")
print("\nYou can login at: http://127.0.0.1:8000/login/")
print("Admin panel: http://127.0.0.1:8000/admin/")
print("="*50)

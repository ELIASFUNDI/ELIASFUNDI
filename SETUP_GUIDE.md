# Photography Studio Management System - Setup Guide

## Overview

This is a comprehensive photography studio management system built with Django. The system allows photographers to manage their business including bookings, client interactions, photo galleries, workflow management, and payment tracking.

## Features

### For Clients
- **User Registration & Authentication**: Secure login and registration system
- **Browse Packages**: View different photography packages with pricing
- **Book Sessions**: Create bookings with date, time, location, and event type
- **Track Progress**: View workflow stages (capture, editing, approval, delivery, achievement)
- **View Photos**: Browse photo galleries from their sessions
- **Select Favorites**: Mark favorite photos for selection
- **Download Photos**: Download high-quality images
- **Comments**: Communicate with photographers through comments

### For Photographers/Admin
- **Dashboard**: View all bookings and assignments
- **Assign Photographers**: Allocate photographers to different sessions
- **Upload Photos**: Upload session photos to client galleries
- **Workflow Management**: Update workflow stages as work progresses
- **View Bookings**: See all client bookings and their details
- **Comment System**: Respond to client comments
- **Payment Tracking**: Track payments and outstanding balances

### System Features
- **Package Management**: Define photography packages with pricing and features
- **Event Types**: Support for weddings, portraits, corporate events, birthdays, etc.
- **Workflow Stages**: Track progress through capture, editing, approval, delivery, and achievement stages
- **Payment System**: Track payments with multiple payment methods
- **Responsive Design**: Bootstrap 5-based responsive interface
- **Admin Panel**: Django admin for managing all data

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite (can be upgraded to PostgreSQL)
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Image Handling**: Pillow
- **Configuration**: python-decouple

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd ELIASFUNDI
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file and set your configuration
# You can use the default values for development
```

### Step 5: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 7: Create Media and Static Directories

```bash
mkdir -p media/profiles media/packages media/session_photos media/thumbnails
mkdir -p static/css static/js
```

### Step 8: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: http://127.0.0.1:8000/

## Initial Setup

### 1. Create Photographer Accounts

After creating your superuser account:

1. Go to http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Go to "User Profiles"
4. Change the user_type from "client" to "photographer" for photographer accounts

### 2. Create Photography Packages

1. In the Django admin, go to "Packages"
2. Click "Add Package"
3. Fill in the details:
   - Name (e.g., "Wedding Basic", "Portrait Premium")
   - Description
   - Price
   - Duration in hours
   - Number of photos included
   - Features (one per line)
   - Upload a package image
4. Mark as "Active"
5. Save

### 3. Test the System

1. Register a new client account at: http://127.0.0.1:8000/register/
2. Browse packages at: http://127.0.0.1:8000/packages/
3. Create a booking
4. Login as photographer to view and manage bookings

## Usage Guide

### Client Workflow

1. **Register/Login**: Create an account or login
2. **Browse Packages**: View available photography packages
3. **Create Booking**: Select a package and fill in booking details
4. **Track Progress**: View booking status in dashboard
5. **View Photos**: Once photographer uploads photos, view them in gallery
6. **Select Favorites**: Mark favorite photos
7. **Download**: Download selected photos
8. **Comment**: Add comments for photographer

### Photographer Workflow

1. **Login**: Access photographer dashboard
2. **View Bookings**: See all bookings or assigned bookings
3. **Assign**: Assign photographers to bookings (if admin)
4. **Update Workflow**: Mark workflow stages as complete
5. **Upload Photos**: Upload session photos to booking
6. **Respond**: Reply to client comments
7. **Manage**: Update booking status and details

## Project Structure

```
ELIASFUNDI/
├── photography_studio/     # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── studio/                 # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── forms.py           # Form definitions
│   ├── admin.py           # Admin configuration
│   ├── urls.py            # URL routing
│   └── signals.py         # Signal handlers
├── templates/             # HTML templates
│   ├── base.html
│   └── studio/
├── static/                # Static files (CSS, JS)
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── README.md             # Project documentation
```

## Database Models

### UserProfile
- Extends Django User model
- Fields: user_type (client/photographer), phone, address, profile_picture

### Package
- Photography packages offered
- Fields: name, description, price, duration, number_of_photos, features, image

### Booking
- Client bookings/sessions
- Fields: client, photographer, package, event_type, event_date, location, status, total_amount

### WorkflowStage
- Workflow tracking for each booking
- Stages: capture, editing, approval, delivery, achievement

### Photo
- Session photos
- Fields: booking, image, title, description, is_approved, is_selected_by_client

### Comment
- Comments on bookings
- Fields: booking, user, content

### Payment
- Payment tracking
- Fields: booking, amount, payment_method, payment_status, transaction_id

## Configuration

### Environment Variables (.env)

```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Production Deployment

For production deployment:

1. Set `DEBUG=False` in .env
2. Add your domain to `ALLOWED_HOSTS`
3. Use PostgreSQL instead of SQLite
4. Configure proper media/static file serving
5. Use a production WSGI server (gunicorn, uWSGI)
6. Set up HTTPS with SSL certificate
7. Configure email backend for notifications

## Troubleshooting

### Images not displaying
- Make sure media directories exist
- Check MEDIA_URL and MEDIA_ROOT in settings.py
- Ensure DEBUG=True or properly configure static file serving

### Database errors
- Run migrations: `python manage.py migrate`
- Check database file permissions

### Permission errors
- Ensure proper file permissions on media directories
- Check user permissions in admin panel

## Support

For issues or questions, contact: eliasdavi965@gmail.com

## Future Enhancements

- Email notifications for booking updates
- Payment gateway integration (Stripe, PayPal)
- Photo editing tools
- Calendar view for bookings
- Photographer availability management
- Client reviews and ratings
- Invoice generation
- SMS notifications
- Cloud storage integration (AWS S3, Google Cloud Storage)
- Mobile app

## License

This project is proprietary software. All rights reserved.

## Credits

Developed by ELIASFUNDI
Email: eliasdavi965@gmail.com

# Photography Studio Management System

A comprehensive web-based photography studio management system built with Django and Python.

## About

This system helps photography studios manage their entire workflow from client bookings to photo delivery. It provides separate interfaces for clients and photographers, making it easy to coordinate photo sessions, track progress, and deliver final products.

## Key Features

- **Client Portal**: Browse packages, book sessions, view galleries, select and download photos
- **Photographer Dashboard**: Manage bookings, upload photos, track workflow stages
- **Package Management**: Define different photography packages with custom pricing
- **Workflow Tracking**: Monitor progress through capture, editing, approval, delivery stages
- **Photo Gallery**: Secure photo viewing and download system
- **Payment Tracking**: Track payments and outstanding balances
- **Commenting System**: Enable communication between clients and photographers
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Technology Stack

- **Backend**: Django 4.2.7, Python 3.8+
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite (development) / PostgreSQL (production)
- **Image Processing**: Pillow

## Quick Start

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed installation and usage instructions.

```bash
# Clone the repository
git clone <repository-url>
cd ELIASFUNDI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit http://127.0.0.1:8000 to access the application.

## Project Structure

```
ELIASFUNDI/
├── photography_studio/     # Django project settings
├── studio/                 # Main application
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript files
├── media/                  # User uploaded files
├── requirements.txt        # Python dependencies
└── SETUP_GUIDE.md         # Detailed documentation
```

## Screenshots

(Add screenshots here after deployment)

## Contributing

This is a personal project. For suggestions or issues, please contact me.

## Contact

**Developer**: ELIASFUNDI
**Email**: eliasdavi965@gmail.com

## License

All rights reserved.

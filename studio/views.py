from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q, Sum
from django.http import HttpResponse, FileResponse
from .models import (
    UserProfile, Package, Booking, WorkflowStage,
    Photo, Comment, Payment
)
from .forms import (
    UserRegistrationForm, BookingForm, CommentForm,
    PaymentForm, PhotoUploadForm, UserProfileForm
)


def home(request):
    """Home page view"""
    packages = Package.objects.filter(is_active=True)[:3]
    context = {
        'packages': packages,
    }
    return render(request, 'studio/home.html', context)


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to our studio.')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()

    return render(request, 'studio/register.html', {'form': form})


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.get_full_name()}!')
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'studio/login.html', {'form': form})


@login_required
def logout_view(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def dashboard(request):
    """Main dashboard view - redirects based on user type"""
    try:
        profile = request.user.profile
        if profile.user_type == 'photographer':
            return redirect('photographer_dashboard')
        else:
            return redirect('client_dashboard')
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=request.user, user_type='client')
        return redirect('client_dashboard')


@login_required
def client_dashboard(request):
    """Client dashboard view"""
    bookings = Booking.objects.filter(client=request.user).select_related('package', 'photographer')
    context = {
        'bookings': bookings,
    }
    return render(request, 'studio/client_dashboard.html', context)


@login_required
def photographer_dashboard(request):
    """Photographer/Admin dashboard view"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if profile.user_type != 'photographer':
        messages.error(request, 'Access denied. Photographer access only.')
        return redirect('client_dashboard')

    assigned_bookings = Booking.objects.filter(photographer=request.user).select_related('client', 'package')
    all_bookings = Booking.objects.all().select_related('client', 'package', 'photographer')

    context = {
        'assigned_bookings': assigned_bookings,
        'all_bookings': all_bookings,
    }
    return render(request, 'studio/photographer_dashboard.html', context)


def packages_list(request):
    """List all available packages"""
    packages = Package.objects.filter(is_active=True)
    return render(request, 'studio/packages_list.html', {'packages': packages})


def package_detail(request, pk):
    """Package detail view"""
    package = get_object_or_404(Package, pk=pk, is_active=True)
    return render(request, 'studio/package_detail.html', {'package': package})


@login_required
def create_booking(request, package_id=None):
    """Create a new booking"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.client = request.user
            booking.total_amount = booking.package.price
            booking.save()

            # Create workflow stages
            stages = ['capture', 'editing', 'approval', 'delivery', 'achievement']
            for stage in stages:
                WorkflowStage.objects.create(booking=booking, stage=stage)

            messages.success(request, 'Booking created successfully!')
            return redirect('booking_detail', pk=booking.pk)
    else:
        initial = {}
        if package_id:
            package = get_object_or_404(Package, pk=package_id, is_active=True)
            initial['package'] = package

        form = BookingForm(initial=initial)

    return render(request, 'studio/create_booking.html', {'form': form})


@login_required
def booking_detail(request, pk):
    """Booking detail view"""
    booking = get_object_or_404(Booking, pk=pk)

    # Check permissions
    profile = request.user.profile
    if booking.client != request.user and profile.user_type != 'photographer':
        messages.error(request, 'You do not have permission to view this booking.')
        return redirect('dashboard')

    photos = booking.photos.all()
    comments = booking.comments.all().select_related('user')
    payments = booking.payments.all()
    workflow_stages = booking.workflow_stages.all()

    total_paid = payments.filter(payment_status='completed').aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'booking': booking,
        'photos': photos,
        'comments': comments,
        'payments': payments,
        'workflow_stages': workflow_stages,
        'total_paid': total_paid,
        'comment_form': CommentForm(),
    }
    return render(request, 'studio/booking_detail.html', context)


@login_required
def add_comment(request, booking_id):
    """Add a comment to a booking"""
    if request.method == 'POST':
        booking = get_object_or_404(Booking, pk=booking_id)

        # Check permissions
        profile = request.user.profile
        if booking.client != request.user and profile.user_type != 'photographer':
            messages.error(request, 'You do not have permission to comment on this booking.')
            return redirect('dashboard')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.booking = booking
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully.')

    return redirect('booking_detail', pk=booking_id)


@login_required
def upload_photos(request, booking_id):
    """Upload photos to a booking - photographer only"""
    booking = get_object_or_404(Booking, pk=booking_id)
    profile = request.user.profile

    if profile.user_type != 'photographer':
        messages.error(request, 'Only photographers can upload photos.')
        return redirect('booking_detail', pk=booking_id)

    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.booking = booking
            photo.save()
            messages.success(request, 'Photo uploaded successfully.')
            return redirect('booking_detail', pk=booking_id)
    else:
        form = PhotoUploadForm()

    return render(request, 'studio/upload_photos.html', {'form': form, 'booking': booking})


@login_required
def select_photo(request, photo_id):
    """Client selects a photo"""
    photo = get_object_or_404(Photo, pk=photo_id)

    if photo.booking.client != request.user:
        messages.error(request, 'You do not have permission to select this photo.')
        return redirect('dashboard')

    photo.is_selected_by_client = not photo.is_selected_by_client
    photo.save()

    status = 'selected' if photo.is_selected_by_client else 'unselected'
    messages.success(request, f'Photo {status} successfully.')

    return redirect('booking_detail', pk=photo.booking.pk)


@login_required
def download_photo(request, photo_id):
    """Download a photo"""
    photo = get_object_or_404(Photo, pk=photo_id)

    # Check permissions
    profile = request.user.profile
    if photo.booking.client != request.user and profile.user_type != 'photographer':
        messages.error(request, 'You do not have permission to download this photo.')
        return redirect('dashboard')

    return FileResponse(photo.image.open(), as_attachment=True, filename=photo.image.name.split('/')[-1])


@login_required
def update_workflow(request, stage_id):
    """Update workflow stage - photographer only"""
    stage = get_object_or_404(WorkflowStage, pk=stage_id)
    profile = request.user.profile

    if profile.user_type != 'photographer':
        messages.error(request, 'Only photographers can update workflow stages.')
        return redirect('booking_detail', pk=stage.booking.pk)

    stage.is_completed = not stage.is_completed
    stage.save()

    status = 'completed' if stage.is_completed else 'reopened'
    messages.success(request, f'Workflow stage {status} successfully.')

    return redirect('booking_detail', pk=stage.booking.pk)


@login_required
def assign_photographer(request, booking_id):
    """Assign a photographer to a booking - photographer only"""
    if request.method == 'POST':
        booking = get_object_or_404(Booking, pk=booking_id)
        profile = request.user.profile

        if profile.user_type != 'photographer':
            messages.error(request, 'Only photographers can assign bookings.')
            return redirect('dashboard')

        photographer_id = request.POST.get('photographer_id')
        if photographer_id:
            photographer = get_object_or_404(UserProfile, pk=photographer_id, user_type='photographer')
            booking.photographer = photographer.user
            booking.status = 'confirmed'
            booking.save()
            messages.success(request, 'Photographer assigned successfully.')

    return redirect('photographer_dashboard')


@login_required
def profile_view(request):
    """View and edit user profile"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'studio/profile.html', {'form': form, 'profile': profile})


@login_required
def gallery_view(request, booking_id):
    """View all photos from a booking"""
    booking = get_object_or_404(Booking, pk=booking_id)

    # Check permissions
    profile = request.user.profile
    if booking.client != request.user and profile.user_type != 'photographer':
        messages.error(request, 'You do not have permission to view this gallery.')
        return redirect('dashboard')

    photos = booking.photos.all()

    context = {
        'booking': booking,
        'photos': photos,
    }
    return render(request, 'studio/gallery.html', context)

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone


class UserProfile(models.Model):
    """Extended user profile for clients and photographers"""
    USER_TYPE_CHOICES = [
        ('client', 'Client'),
        ('photographer', 'Photographer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='client')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.user_type})"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class Package(models.Model):
    """Photography packages offered by the studio"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    duration_hours = models.IntegerField(help_text="Duration in hours")
    number_of_photos = models.IntegerField(help_text="Number of edited photos included")
    features = models.TextField(help_text="List of features (one per line)")
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

    class Meta:
        ordering = ['price']


class Booking(models.Model):
    """Booking/Session management"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    EVENT_TYPE_CHOICES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('portrait', 'Portrait'),
        ('corporate', 'Corporate Event'),
        ('family', 'Family Photo'),
        ('graduation', 'Graduation'),
        ('other', 'Other'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    photographer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='assigned_bookings')
    package = models.ForeignKey(Package, on_delete=models.PROTECT)

    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    special_requests = models.TextField(blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.client.get_full_name()} - {self.event_type}"

    class Meta:
        ordering = ['-event_date']


class WorkflowStage(models.Model):
    """Workflow stages for photo shoot process"""
    STAGE_CHOICES = [
        ('capture', 'Capture'),
        ('editing', 'Editing'),
        ('approval', 'Client Approval'),
        ('delivery', 'Delivery'),
        ('achievement', 'Achievement/Completed'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='workflow_stages')
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        status = "Completed" if self.is_completed else "In Progress"
        return f"{self.booking.id} - {self.stage} ({status})"

    def save(self, *args, **kwargs):
        if self.is_completed and not self.completed_at:
            self.completed_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['booking', 'stage']
        unique_together = ['booking', 'stage']


class Photo(models.Model):
    """Photos from a booking/session"""
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='session_photos/%Y/%m/%d/')
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    is_approved = models.BooleanField(default=False)
    is_selected_by_client = models.BooleanField(default=False)

    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Photo {self.id} - Booking #{self.booking.id}"

    class Meta:
        ordering = ['-uploaded_at']


class Comment(models.Model):
    """Comments on bookings/sessions"""
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.get_full_name()} on Booking #{self.booking.id}"

    class Meta:
        ordering = ['-created_at']


class Payment(models.Model):
    """Payment tracking for bookings"""
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Credit/Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('mobile_money', 'Mobile Money'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=200, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Payment #{self.id} - Booking #{self.booking.id} - ${self.amount}"

    class Meta:
        ordering = ['-payment_date']

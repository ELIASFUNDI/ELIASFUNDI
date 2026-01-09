from django.contrib import admin
from .models import (
    UserProfile, Package, Booking, WorkflowStage,
    Photo, Comment, Payment
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'phone', 'created_at']
    list_filter = ['user_type', 'created_at']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration_hours', 'number_of_photos', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']


class WorkflowStageInline(admin.TabularInline):
    model = WorkflowStage
    extra = 0


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'photographer', 'package', 'event_type', 'event_date', 'status']
    list_filter = ['status', 'event_type', 'event_date', 'created_at']
    search_fields = ['client__username', 'photographer__username', 'location']
    inlines = [WorkflowStageInline, PaymentInline]
    date_hierarchy = 'event_date'


@admin.register(WorkflowStage)
class WorkflowStageAdmin(admin.ModelAdmin):
    list_display = ['booking', 'stage', 'is_completed', 'completed_at']
    list_filter = ['stage', 'is_completed', 'completed_at']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'booking', 'title', 'is_approved', 'is_selected_by_client', 'uploaded_at']
    list_filter = ['is_approved', 'is_selected_by_client', 'uploaded_at']
    search_fields = ['title', 'description']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'booking', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'user__username']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'booking', 'amount', 'payment_method', 'payment_status', 'payment_date']
    list_filter = ['payment_status', 'payment_method', 'payment_date']
    search_fields = ['transaction_id']

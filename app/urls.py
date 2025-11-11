
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import gallery_view

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
      

    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),


  # Profile
    path('profile/', views.profile, name='profile'),

    # User Management
    path('register-user/', views.register_user, name='register_user'),
    
    # Website Management
    path('manage-website/', views.manage_website, name='manage_website'),
    path('gallery-list/', views.gallery_list, name='gallery_list'),
    path('services-list/', views.service_list, name='service_list'),
    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('video-testimonials/', views.video_testimonial_list, name='video_testimonial_list'), 
    
    path('manage-banner/', views.manage_banner, name='manage_banner'),
    path('contact-messages/', views.contact_messages_view, name='contact_messages'),
    path('delete-message/<int:pk>/', views.delete_contact_message, name='delete_contact_message'),
    path('bank-details/', views.bank_detail_update, name='bank_detail_update'),
    
    path('manage-event-videos/', views.manage_event_videos, name='manage_event_videos'),
    path('delete-event-video/<int:video_id>/', views.delete_event_video, name='delete_event_video'),
    path('events/', views.events_page, name='events_page'),

    path('contact/', views.contact_view, name='contact'),
    path('testimonial/', views.testimonial_view, name='testimonial'),   
    path('about/', views.about_view, name='about'),
    path('gallery/', gallery_view, name='gallery'),
    path('404/', views.Error_view, name='error_404'),

    # Staff
    path('add_staff/', views.add_staff, name='add_staff'),
    path('staff_list/', views.staff_list, name='staff_list'),
    path('staff/<int:staff_id>/edit/', views.edit_staff, name='edit_staff'),
    path('staff/<int:staff_id>/delete/', views.delete_staff, name='delete_staff'),
    path('staff/<int:staff_id>/', views.staff_detail, name='staff_detail'),

    # Salary
    path('base/', views.base, name='base'),
    path('add_salary/', views.add_salary, name='add_salary'),
    path('salary_list/', views.salary_list, name='salary_list'),
    path('salary/<int:id>/edit/', views.edit_salary, name='edit_salary'),
    path('staff_search/', views.staff_search, name='staff_search'),

    # Billing
    path('bills/', views.bill_list, name='bill_list'),
    path('bills/create/', views.create_bill, name='create_bill'),
    path('bills/<int:bill_id>/edit/', views.edit_bill, name='edit_bill'),
    path('ajax/get-product-rate/', views.get_product_rate, name='get_product_rate'),
    path('bills/<int:bill_id>/', views.bill_detail, name='bill_detail'),
    path('bills/<int:bill_id>/delete/', views.delete_bill, name='delete_bill'),
    path('bills/<int:bill_id>/reminder/', views.send_reminder, name='send_reminder'),


    # Products
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),

    #income
    path('income/', views.income_dashboard, name='income_dashboard'),
    path('income/export/<str:file_type>/', views.export_income, name='export_income'),


    # Expense URLs (append)
    path('expenses/', views.expense_dashboard, name='expense_dashboard'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/export/<str:file_type>/', views.export_expenses, name='export_expenses'),


    # AJAX
    path('ajax/get-staff-salary/', views.ajax_get_staff_salary, name='ajax_get_staff_salary'),
    path('ajax/add-expense-category/', views.ajax_add_category, name='ajax_add_expense_category'),

]


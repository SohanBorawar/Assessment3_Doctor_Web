from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('doctor-signup/',views.doctor_signup,name='doctor-signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forget-password/',views.forget_password,name='forget-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('appointment/',views.appointment,name='appointment'),
    path('appointment-request/',views.appointment_request,name='appointment-request'),
    path('appointment-approval/',views.appointment_approval,name='appointment-approval'),
    path('my_appointment/',views.my_appointment,name='my_appointment'),


]
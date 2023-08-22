from django.shortcuts import render,redirect
from .models import Contact,Patient,Doctor,Appointment


from django.conf import settings
from django.core.mail import send_mail

import random
import datetime

# Create your views here.

def index(request):
    doctor = Doctor.objects.all()
    index_doctor = []
    for i in doctor[0:4]:
        index_doctor.append(i)
    print(index_doctor)
    return render(request,'index.html',{'index_doctor':index_doctor})

def contact(request):
    if request.method=='POST':
        Contact.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        subject = request.POST['subject'],
        message = request.POST['message'],
        )
        succ_msg = 'Message send Successfully'
        return render(request,'contact.html',{'succ_msg':succ_msg})
    else:
        return render(request,'contact.html')

def signup(request):
    if request.method=='POST':
        try:
            patient = Patient.objects.get(email = request.POST['email'])
            info_msg = 'Entered Email Is Already Registered'
            return render(request,'signup.html',{'info_msg':info_msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                Patient.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    gender = request.POST['gender'],
                    age = request.POST['age'],
                    password = request.POST['password'],
                    address = request.POST['address'],
                    profile_pic = request.FILES['profile_pic'],
                )  
                succ_msg = 'User Registered Successfully'
                return render(request,'signup.html',{'succ_msg':succ_msg})
            else:
                err_msg = 'password & confirm Password Does Not Match'
                return render(request,'signup.html',{'err_msg':err_msg})
    else:
        return render(request,'signup.html')
    
def doctor_signup(request):
    if request.method=='POST':
        try:
            try:
                doctor = Doctor.objects.get(email = request.POST['email'])
                info_msg = 'Entered Email Is Already Registered'
                return render(request,'doctor-signup.html',{'info_msg':info_msg})
            except:
                Patient.objects.get(email = request.POST['email'])
                info_msg = 'Entered Email Is Already Registered'
                return render(request,'doctor-signup.html',{'info_msg':info_msg})  
        except:
            if request.POST['password'] == request.POST['cpassword']:
                Doctor.objects.create(
                    name = request.POST['name'],
                    qualification = request.POST['qualification'],
                    speciality = request.POST['speciality'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    gender = request.POST['gender'],
                    password = request.POST['password'],
                    profile_pic = request.FILES['profile_pic']
                )  
                succ_msg = 'User Registered Successfully'
                return render(request,'doctor-signup.html',{'succ_msg':succ_msg})
            else:
                err_msg = 'password & confirm Password Does Not Match'
                return render(request,'doctor-signup.html',{'err_msg':err_msg})
    else:
        return render(request,'doctor-signup.html')
    
def login(request):
    if request.method=='POST':
        print(request.POST['email'])
        try:
            try:
                doctor = Doctor.objects.get(email = request.POST['email'])
                if doctor.password == request.POST['password']:
                    request.session['doctor_email'] = doctor.email
                    return render(request,'index.html')
                else:
                    err_msg = 'Password & Confirm Password Does Not Match'
                    return render(request,'login.html',{'err_msg':err_msg})
            except:
                patient = Patient.objects.get(email = request.POST['email'])
                if patient.password == request.POST['password']:
                    request.session['email']=patient.email
                    return render(request,'index.html')
                else:
                    err_msg = 'Password & Confirm Password Does Not Match'
                    return render(request,'login.html',{'err_msg':err_msg})
        except:
            err_msg = 'Email Not Registered'
            return render(request,'login.html',{'err_msg':err_msg})
    else:    
        return render(request,'login.html')
    
def logout(request):
    try:
        try:
            del request.session['email']
            return redirect('index')
        except:
            del request.session['doctor_email']
            return redirect('index')
    except:
        return render(request,'index.html')    
    
def forget_password(request):
    if request.method=='POST':
        try:
            try:
                print('try2')
                doctor = Doctor.objects.get(email = request.POST['email'])
                otp = random.randint(1000,9999)
                subject = 'Otp To Reset Password'
                message = f'Hi {doctor.name}, thank you for registering with Us {otp}.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [doctor.email, ]
                send_mail( subject, message, email_from, recipient_list )

                succ_msg = 'OTP Send Successfullt'
                return render(request,'verify-otp.html',{'succ_msg':succ_msg,'email':doctor.email,'otp':otp})
            except:
                print('exce 2')
                patient = Patient.objects.get(email = request.POST['email'])    
                otp = random.randint(1000,9999)
                subject = 'Otp To Reset Password'
                message = f'Hi {patient.name}, thank you for registering with Us {otp}.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [patient.email, ]
                send_mail( subject, message, email_from, recipient_list )

                succ_msg = 'OTP Send Successfullt'
                return render(request,'verify-otp.html',{'succ_msg':succ_msg,'email':patient.email,'otp':otp})
        except Exception as e:
            print(e)
            err_msg = 'Email Not Registered'
            return render(request,'signup.html',{'err_msg':err_msg})       
    else:
        return render(request,'forget-password.html')

def verify_otp(request):
    email = request.POST['email']
    gotp = request.POST['uotp']
    otp = request.POST['otp']

    if gotp == otp:
        return render(request,'new-password.html',{'email':email})
    else:
        err_msg = 'Incorrect OTP'
        return render(request,'verify-otp.html',{'err_msg':err_msg,'email':email,'otp':gotp})

def new_password(request):
    email = request.POST['email']
    np = request.POST['newpassword']    
    cnp = request.POST['cnewpassword']
    try:
        doctor = Doctor.objects.get(email = email)
        if np == cnp:
            doctor.password = np
            doctor.save()
            succ_msg = 'Password Changed Successfully'
            return render(request,'login.html',{'succ_msg':succ_msg})
        else:
            err_msg = 'Password & Confirm Password Does Not Match'
            return render(request,'new-password.html',{'err_msg':err_msg,'email':email})
    except:
        patient = Patient.objects.get(email = email)
        if np == cnp :
            patient.password = np
            patient.save()
            succ_msg = 'Password Changed Successfully'
            return render(request,'login.html',{'succ_msg':succ_msg})
        else:
            err_msg = 'Password & Confirm Password Does Not Match'
            return render(request,'new-password.html',{'err_msg':err_msg,'email':email})

def appointment(request):

    if request.method=='POST':
        patient = Patient.objects.get(email = request.session['email'])
        doctor = Doctor.objects.get(pk = request.POST['doctor'])
        print(doctor)
        current_datetime = datetime.datetime.now()
        datetime_format = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        Appointment.objects.create(
            Doctor = doctor,
            patient = patient,
            profile_pic = patient.profile_pic.url,
            name = request.POST['name'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            doctor_field = request.POST['doctor_field'],
            appointment_date = request.POST['appointment_date'],
            appointment_time = request.POST['appointment_time'],
            date_time = datetime_format,
        )
        succ_msg = 'Appoinment Request Applied Successfully'
        return render(request,'appointment.html',{'succ_msg':succ_msg})

    else:
        patient = Patient.objects.get(email = request.session['email'])
        doctor = Doctor.objects.all()
        print(doctor)
        return render(request,'appointment.html',{'patient':patient,'doctor':doctor})
    
def appointment_request(request):
        doctor = Doctor.objects.get(email = request.session['doctor_email'])
        appointment_request = Appointment.objects.filter(pk = doctor.pk)
        print(appointment_request)
        appointment_flag = False
        return render(request,'appointment-request.html',{'appointment_request':appointment_request,'appointment_flag':appointment_flag})
def appointment_approval(request):
    doctor = Doctor.objects.get(email = request.session['doctor_email'])
    appointment_request = Appointment.objects.filter(pk = doctor.pk)
    appointment_approval = Appointment.objects.get(pk = request.POST['pk'])
    if appointment_approval.appointment_request == True :
        appointment_flag = True
    else:
        appointment_approval.appointment_request = True
        appointment_approval.save()
        appointment_flag = True
    return render(request,'appointment-request.html',{'appointment_request':appointment_request,'appointment_flag':appointment_flag})

def my_appointment(request):
    patient = Patient.objects.get(email = request.session['email'])
    appointments = Appointment.objects.filter(patient = patient)
    return render(request,'my-appointment.html',{'appointments':appointments})


    
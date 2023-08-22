from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name + "-" + self.subject

class Patient(models.Model):

    profile_pic = models.ImageField(upload_to='profile_pic/',default='')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    gender = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=1)
    password = models.CharField(max_length=100)
    address = models.TextField()


    def __str__(self) -> str:
        return self.name + '-' + self.email
    
class Doctor(models.Model):

    profile_pic = models.ImageField(upload_to='profile_pic/')
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100,default='')
    speciality = models.CharField(max_length=100,default='')
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    gender = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name + '-' + self.speciality

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='appointment_user/')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    doctor_field = models.CharField(max_length=100)
    appointment_date = models.CharField(max_length=100,default='')
    appointment_time = models.CharField(max_length=100,default='')
    date_time = models.DateTimeField()
    appointment_request = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.patient.name + " " + self.Doctor.name

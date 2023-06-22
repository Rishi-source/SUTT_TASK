from django.db import models
from django.contrib.auth.models import User 
DOCTOR_CHOICES = [
    ('Cardiologist', 'Cardiologist'),
    ('Dermatologist', 'Dermatologist'),
    ('Endocrinologist', 'Endocrinologist'),
    ('Gastroenterologist', 'Gastroenterologist'),
    ('Neurologist', 'Neurologist'),
    ('Oncologist', 'Oncologist'),
    ('Pediatrician', 'Pediatrician'),
    ('Psychiatrist', 'Psychiatrist'),
    ('Radiologist', 'Radiologist'),
    ('Surgeon', 'Surgeon'),
    ('Orthopedic Surgeon', 'Orthopedic Surgeon'),
    ('Ophthalmologist', 'Ophthalmologist'),
    ('ENT Specialist', 'ENT Specialist'),
    ('Urologist', 'Urologist'),
    ('Nephrologist', 'Nephrologist'),
    ('Pulmonologist', 'Pulmonologist'),
    ('Allergist/Immunologist', 'Allergist/Immunologist'),
    ('Rheumatologist', 'Rheumatologist'),
    ('Hematologist', 'Hematologist'),
    ('Osteopath', 'Osteopath'),
    ('Chiropractor', 'Chiropractor'),
    ('Homeopath', 'Homeopath'),
    ('Ayurvedic Doctor', 'Ayurvedic Doctor'),
    ('Naturopath', 'Naturopath'),
    ('Physiotherapist', 'Physiotherapist'),
    ('Dentist', 'Dentist'),
    ('Veterinarian', 'Veterinarian'),
]
class register_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profiles/%Y/%m/%d", null=True, blank=True)
    age = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=250, default="Male")
    address = models.CharField(max_length=250, null=True, blank=True)
    occupation = models.CharField(max_length=250, null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    update_on = models.DateTimeField(auto_now=True, null=True)
    Type_of_Doctor = models.CharField(max_length=250 , choices=DOCTOR_CHOICES)

    def __str__(self):
        return self.user.username
class appointment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     details = models.ForeignKey(register_table , null = True , on_delete=models.CASCADE,blank=True)
     name = models.CharField(max_length=50, null=True, blank=True)
     age = models.CharField(max_length=250, null=True, blank=True)
     gender = models.CharField(max_length=250, default="Male")
     problem = models.CharField(max_length=550, null=True, blank=True)
     Day_slot =models.DateField(null=True)
     time_slot=models.TimeField(null=True)
     Type_of_Doctor_you_want_to_consult = models.CharField(max_length=250, default="Select",choices=DOCTOR_CHOICES)
     status = models.BooleanField(default = False)
     def __str__(self):
      return self.user.username 






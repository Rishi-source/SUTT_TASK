from django import forms
from app.models import appointment


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]
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



class appointment_form(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    Type_of_Doctor_you_want_to_consult = forms.ChoiceField(choices=DOCTOR_CHOICES )

    class Meta:
        model = appointment

        fields = ["name", "age", "gender", "problem",
                  "Day_slot", "time_slot", "Type_of_Doctor_you_want_to_consult"]
        widgets = {
            'Day_slot': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.TimeInput(attrs={'type': 'time'}),
            'problem': forms.Textarea(attrs={'rows': 4}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import MeterReading

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    staffno = forms.CharField(
        max_length=6, 
        required=True, 
        help_text="Enter your BSL Staff Number (6 digits)."
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'staffno', 'password1', 'password2')

    def clean_staffno(self):
        staffno = self.cleaned_data.get('staffno')
        if not staffno.isdigit() or len(staffno) != 6:
            raise forms.ValidationError("BSL Staff No. must be exactly 6 digits.")
        return staffno


# forms.py

# electricmeter_reading/forms.py



class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['slno', 'quarterno', 'meterreading', 'meterimage', 'submit_option']

from django import forms 
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
    }))
    class Meta: 
        model = Account 
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

# give a class form control to the registration form from bootstrap
    def __init__(self, *args, **kwargs):
     super(RegistrationForm, self).__init__(*args, **kwargs)
     # place holders for the registration
     self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
     self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
     self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
     self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
     for field in self.fields:
        self.fields[field].widget.attrs['class'] = 'form-control'

    # make sure password and confirm password matches 
    def clean(self):
       cleaned_data = super(RegistrationForm, self).clean()
       password = cleaned_data.get('password')
       confirm_password = cleaned_data.get('confirm_password')

       if password != confirm_password:
          raise forms.ValidationError(
             "Password does not match!"
          )

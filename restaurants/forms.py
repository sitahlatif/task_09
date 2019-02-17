from django import forms
from .models import Restaurant
from django.contrib.auth.models import User

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }
class SignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields=['username', 'email', 'password']

		widgets={
		'password': forms.PasswordInput()
		}
class SignInForm(forms.Form):
	username=forms.CharField(required=True)
	password=forms.CharField(required=True, widget=forms.PasswordInput())
		
		
			

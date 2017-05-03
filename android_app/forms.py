from django import forms
from android_app.models import Auth

class AuthForm(forms.ModelForm):
	
	class Meta:
		model = Auth
		fields = ['p_user', 'p_pass']


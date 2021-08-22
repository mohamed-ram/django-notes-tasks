from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q

from .models import UserAccount


User = get_user_model()


# creation form.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    
    
    class Meta:
        model = UserAccount
        fields = ('username', 'email')
        
        labels = {
            "username": "User Name",
        }
        
        error_messages = {
            'username':  {
                'unique': "User name must be unique"
            }
        }
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        if commit:
            user.save()
        return user


# Login Form,
class LoginForm(forms.Form):
    query = forms.CharField(label="Username or Email")
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        
        user_qs = User.objects.filter(
            Q(username__iexact=query) |
            Q(email__iexact=query)
        ).distinct().first()
        
        if not user_qs and user_qs.count() != 1:
            raise forms.ValidationError("invalid user name")
        
        if not user_qs.is_active:
            raise forms.ValidationError("inactive account.. you must verify your account")
        
        if not user_qs.check_password(password):
            raise forms.ValidationError("invalid password")
        return super().clean()

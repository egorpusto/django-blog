from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password_confirm = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def clean_password_confirm(self):
        cd = self.cleaned_data
        if cd.get("password") != cd.get("password_confirm"):
            raise forms.ValidationError("Passwords don't match.")
        return cd["password_confirm"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

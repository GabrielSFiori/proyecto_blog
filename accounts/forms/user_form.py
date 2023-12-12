from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import UserModel


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ['username', 'password']

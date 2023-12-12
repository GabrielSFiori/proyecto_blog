from ..models import User
from django import forms


class BusquedaUserForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50, required=False, label="Apellido del estudiante")

    class Meta:
        model = User
        exclude = ['name', 'email']


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'profile_picture']
        labels = {
            'name': 'Nombre',
            'email': 'Correo electrónico',
            'profile_picture': 'Imagen de perfil',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese su correo'}),
            'profile_picture': forms.ClearableFileInput(attrs={'placeholder': 'Seleccione una imagen de perfil'}),
        }

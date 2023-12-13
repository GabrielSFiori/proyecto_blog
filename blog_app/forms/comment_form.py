from django import forms
from ..models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'author')
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'content': forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí...'}),
        }
        labels = {
            'author': 'Autor',
            'content': 'Contenido',
        }

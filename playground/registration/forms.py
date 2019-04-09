from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Longitud máxima 254 caracteres y debe ser válido.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    # Validación de email único.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('La dirección de email ya se encuentra asociada a un usuario.')

        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Biografía'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enlace Personal'}),  
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido. Longitud máxima 254 caracteres y debe ser válido.')

    class Meta:
        model = User
        fields = ['email']
    
    # Validación de email único.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # Si el email actual se ha actualizado.
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('La dirección de email ya se encuentra asociada a un usuario.')

        return email
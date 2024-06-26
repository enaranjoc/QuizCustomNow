from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
        error_messages={'required': 'Este campo es obligatorio.', 'max_length':'El nombre de usuario no puede exceder los 150 caracteres.'}
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        error_messages={'required': 'Este campo es obligatorio.', 'invalid': 'Introduce una dirección de correo electrónico válida.'}
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
        error_messages={'required': 'Este campo es obligatorio.', 'password_mismatch': 'Las contraseñas no coinciden.'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        error_messages = {
            'password_mismatch': 'Las contraseñas no coinciden.',
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Esto asegura que el mensaje de error de password_mismatch esté presente
        self.fields['password2'].error_messages.update({
            'password_mismatch': 'Las contraseñas no coinciden.'
        })

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.fields['password2'].error_messages['password_mismatch'],
                code='password_mismatch',
            )

        return password2

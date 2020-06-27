from django import forms
from django.core import validators


class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Titulo",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Mete el titulo",
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, "El titulo tiene que ser mayor a 4 caracteres"),
            
            # Contiene expresiones regulares, admite el abcdario con numeros y espacio, esto se aplicara si required esta a True
            validators.RegexValidator('^[A-Za-z0-9 ]*$', "El titulo esta mal formado", "invalid_title")
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea(
            attrs={
                'placeholder':"Mete el contenido",
                'class':"contenido_form_article"
            }
        ),
        validators = [
            validators.MinLengthValidator(50, "Te has pasado, no quiero leer tanto")
        ]
    )

    public_options = [
        (0, "No"),
        (1, "Si")
    ]

    public = forms.TypedChoiceField(
        label = "Publicado??",
        choices = public_options
    )
from .models import user
from django.forms import ModelForm, TextInput

class userform(ModelForm):
    class Meta:
        model = user
        fields = ['talent', 'mail', 'epicid', 'overwatchname', 'teamplay', 'teamplayfn', 'teamplayow', 'nickfn', 'icon', 'date',]  #  'teamplay', 'teamplayfn', 'teamplayow', 'nickfn', 'icon'
        widgets = {
            "talent": TextInput(attrs={
                'class': 'inp',
                "placeholder": 'Enter your TalentID'
            }),
            "mail": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter your mail'
            }),
            "epicid": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter your epicid'
            }),
            "overwatchname": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter your overwatchname'
            }),
            "teamplay": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter1'
            }),
            "teamplayfn": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter2'
            }),
            "teamplayow": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter3'
            }),
            "nickfn": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter4'
            }),
            "icon": TextInput(attrs={
                'class': 'inp',
                'placeholder': 'Enter5'
            }),
        }
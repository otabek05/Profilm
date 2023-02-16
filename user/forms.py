from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


class User_from(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),

    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,

    )
    class Meta:
        model=User
        fields= ['username', 'email' , 'password1','password2']

    def __init__(self, *args, **kwargs):
        super(User_from, self).__init__(*args, **kwargs)

        # Forma sohasiga bitta bitta murojaat etish
        # self.fields['title'].widget.attrs.update({'class': 'form-control'})
        # self.fields['description'].widget.attrs.update({'class': 'form-control'})

        # formaning har bir sohasiga 'form-control' class ini for tsikli yordamida qo'shib chiqish
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

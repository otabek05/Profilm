from . import models

from django.forms import ModelForm, Form



class FilmCreate(ModelForm):
    class Meta:
        model=models.Film
        fields=['title', 'description','category', 'img']
    def __init__(self, *args, **kwargs):
        super(FilmCreate, self).__init__(*args, **kwargs)
        
        # Forma sohasiga bitta bitta murojaat etish
        # self.fields['title'].widget.attrs.update({'class': 'form-control'})
        # self.fields['description'].widget.attrs.update({'class': 'form-control'})
        
        # formaning har bir sohasiga 'form-control' class ini for tsikli yordamida qo'shib chiqish
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
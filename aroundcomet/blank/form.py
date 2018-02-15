from django import forms
from django.utils.timezone import now
from django.core.validators import RegexValidator
from .models import Profile
from django.contrib.auth.admin import User
from django.core.exceptions import ValidationError
import re
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

#                           --- Создание форм с валидацией  данных ---

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'patronymic', 'address', 'flat' , 'home' , 'contact_number', 'date_creating', 'prefering_connection', 'tarrif', 'status']
    date_creating = forms.DateField(initial=now, disabled=True, label='Дата регистрации')
    name = forms.RegexField(regex=r'^\D+$', error_messages={'invalid':'Имя не должно содержать цифр'}, label='Имя', widget=forms.TextInput({"placeholder": 'Имя', 'class':'form-control'}))
    surname = forms.RegexField(regex=r'^\D+$', error_messages={'invalid':'Фамилия не должна содержать цифр'}, label='Фамилия', widget=forms.TextInput({"placeholder": 'Фамилия', 'class':'form-control'}),)
    patronymic = forms.RegexField(regex=r'^\D+$', error_messages={'invalid': 'Отчество не должно содержать цифр'}, label='Отчество', widget=forms.TextInput({"placeholder": 'Отчество', 'class':'form-control'}))
    address = forms.RegexField(regex=r'^\D+$', error_messages={'invalid': 'Массив/Улица не должны содержать цифр'}, label='Массив', widget=forms.TextInput({"placeholder": 'Массив/Улица', 'class':'form-control'}), required=True)
    flat = forms.RegexField(regex=r'^\d+\w+$', error_messages={'invalid':'Поле должно начинаться с цифры'}, label='Квартира', widget=forms.TextInput({"placeholder": 'Квартира', 'class':'form-control'}),)
    home = forms.RegexField(regex=r'^\d+\w+$', error_messages={'invalid':' Поле должно начинаться с цифры'}, label='Дом', widget=forms.TextInput({"placeholder": 'Дом', 'class':'form-control'}),)
    contact_number = forms.RegexField(regex=r'^\+?998\d{9,15}$', error_messages={'invalid':'Номер должен начинаться с +998'}, label='Номер', widget=forms.TextInput({"placeholder": 'Контактный номер', 'class':'form-control'}),)
    prefering_connection = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date', 'class':'form-control'}),label='Дата')
    tarrif = forms.ChoiceField(choices=Profile.tarrif_plans, label='Тарифный план',widget=forms.Select(attrs={'class':'form-control'}))
    status = forms.ChoiceField(choices=Profile.blank_status, label='Статус',widget=forms.Select(attrs={'class':'form-control'}))

'''
       
                            --- Альтернативная валидация полей с помоью методов ---
    
    #managers = forms.ModelChoiceField(queryset=User.objects.all()) Форма для выбора менеджера из выпадающего списка
    #contact_number = forms.CharField(label='' , max_length=15 , widget=forms.TextInput({"placeholder": 'Контанктный номер '}))
    #name = forms.CharField(label='', max_length=15 , required=True, widget=forms.TextInput({"placeholder": 'Имя'}))
    #surname = forms.CharField(label='',max_length=15, widget=forms.TextInput({"placeholder":"Фамилия"}))
    #patronymic = forms.CharField(label='', max_length=20, widget=forms.TextInput({"placeholder": 'Отчество'}))
    #home = forms.CharField(label='',max_length=3, widget=forms.TextInput({"placeholder":'Номер дома'}),)
    #flat = forms.CharField(label='', max_length=3 ,widget=forms.TextInput({"placeholder":'Номер квартиры'}))
    
    def clean_name(self):
        if self.cleaned_data['name'] != re.search('\D+', self.cleaned_data['name']).group():
            raise ValidationError('Name Error')
        return self.cleaned_data


    def clean_surname(self):
        if self.cleaned_data.get('surname') != re.search('\D+', self.cleaned_data.get('surname')).group():
            raise ValidationError("Surname error")
        return self.cleaned_data

    def clean_patronymic(self):
        if self.cleaned_data.get('patronymic') != re.search('\D+', self.cleaned_data.get('patronymic')).group():
            raise ValidationError("patronymic error")
        return self._cleaned_data
    
    
    def clean_home(self):
        if self.cleaned_data.get('home')[0] not in str([ _ for _ in range(0,10)]):
             raise ValidationError('Поле  должно начинаться с цифры , например 108')
        return self.cleaned_data'''




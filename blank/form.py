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
    name = forms.RegexField(regex=r'^\D+$', error_messages={'invalid':'Имя не должно содержать цифр'}, label='', widget=forms.TextInput({"placeholder": 'Имя'}),)
    surname = forms.RegexField(regex=r'^\D+$', error_messages={'invalid':'Фамилия не должна содержать цифр'}, label='', widget=forms.TextInput({"placeholder": 'Фамилия'}),)
    patronymic = forms.RegexField(regex=r'^\D+$', error_messages={'invalid': 'Отчество не должно содержать цифр'}, label='', widget=forms.TextInput({"placeholder": 'Отчество'}),)
    address = forms.RegexField(regex=r'^\D+$', error_messages={'invalid': 'Массив/Улица не должны содержать цифр'}, label='', widget=forms.TextInput({"placeholder": 'Массив/Улица'}), required=True)
    flat = forms.RegexField(regex=r'^\d+\w+$', error_messages={'invalid':'Поле должно начинаться с цифры'}, label='', widget=forms.TextInput({"placeholder": 'Квартира'}),)
    home = forms.RegexField(regex=r'^\d+\w+$', error_messages={'invalid':' Поле должно начинаться с цифры'}, label='', widget=forms.TextInput({"placeholder": 'Дом'}),)
    contact_number = forms.RegexField(regex=r'^\+?998\d{9,15}$', error_messages={'invalid':'Номер должен начинаться с +998'}, label='', widget=forms.TextInput({"placeholder": 'Контанктный номер '}),)
    prefering_connection = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    tarrif = forms.ChoiceField(choices=Profile.tarrif_plans, label='Тарифный план',)
    status = forms.ChoiceField(choices=Profile.blank_status, label='Статус', )
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




from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.contrib.auth.models import User
from .models import Profile
import django_filters
from django import forms
from .views import Main




#                        --- Создание форм для странички search ---

class UserFilter(LoginRequiredMixin ,django_filters.FilterSet):

    date_creating = django_filters.DateFilter(lookup_expr='exact',widget=forms.widgets.DateInput(attrs={'type': 'date'}),label='Дата создания')
    name = django_filters.CharFilter(lookup_expr='icontains',label='Имя')
    surname = django_filters.CharFilter(lookup_expr='icontains',label='Фамилия')
    address = django_filters.CharFilter(lookup_expr='icontains',label='Адрес')
    manager = django_filters.ModelChoiceFilter(queryset=User.objects.all(),label='Менеджер')
    status = django_filters.ChoiceFilter(choices=Profile.blank_status,label='Статус')
    tarrif = django_filters.ChoiceFilter(choices=Profile.tarrif_plans, label='Тариф')
    datetimerange = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}),label='Дата \'С\' - \'До\' ')
    class Meta:
        model = Profile
        fields = []
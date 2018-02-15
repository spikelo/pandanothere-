from django.db import models
from django.utils.timezone import now
from django.contrib.auth.admin import User
from django.urls import reverse
from django.utils.html import format_html
#import datetime

class Profile(models.Model):
    date_creating = models.DateField(help_text='Дата регистрации', null=True, blank=True, default=now)
    name = models.CharField(help_text='Введите имя абонента', max_length=15)
    surname = models.CharField(help_text='Введите фамилию абонента',max_length=15)
    patronymic = models.CharField(help_text='Введите отчество абонента', max_length=20)
    #passport_data = models.CharField(help_text='Паспортные данные',max_length=100)
    address = models.CharField(help_text='Улица/Массив', max_length=20,)
    home = models.CharField(help_text='Введите номер дома', max_length=5)
    flat = models.CharField(help_text='Введите номер квартиры', max_length=5,)
    contact_number = models.CharField(help_text='Контактный номер абонента', max_length=30,)
    prefering_connection = models.DateField(help_text='Предпочитаемая дата подключения')
    datetimerange = models.DateField(help_text='Для фильтрации дат с отметками , ОТ -- К', null=True, blank=True, default=now)
    manager = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL,)

    class Meta:
        permissions = (
            ("can_see_all_blank" , "View all blanks"),
                      )

    tarrif_plans = (
        ('Скоростной 40', 'Скоростной 40'),
        ('Скоростной 60', 'Скоростной 60'),
        ('Скоростной 80', 'Скоростной 80'),
        ('Скоростной 100', 'Скоростной 100'),
        ('Скоростной 120','Скоростной 120'),
        ('Скоростной 140', 'Скоростной 140'),
        ('Скоростной 160', 'Скоростной 160'),
        ('Скоростной 200', 'Скоростной 200'),
        ('Скоростной 240', 'Скоростной 240'),
    )

    tarrif = models.CharField(blank=True ,choices= tarrif_plans , null=True , max_length=15)


    blank_status = (
        ('Открыта', 'Открыта'),
        ('Закрыта', 'Закрыта'),
                    )

    status = models.CharField(max_length=15, choices=blank_status, blank=True , null=True)



    def get_absolute_url(self):
        return reverse('my-ticket', args=[str(self.id)])



    def get_edit_url(self):
        return reverse('edit', args=[str(self.id)])



    def __str__(self):
        return self.name + " "+" "+ self.surname



    def colored_status(self):
        if self.status == 'Открыта':
            return format_html(
                '<span style="color: #006400;">{}</span>',
                self.status
        )

        else:
            return format_html(
                '<span style="color: #FF0000;">{}</span>',
                self.status
        )





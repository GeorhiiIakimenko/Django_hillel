from django.db import models
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField("Name", max_length=30, unique=True)
    description = RichTextField('Description')


    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField("Назава товару", max_length=200, unique=True)
    description = RichTextField('Характеристики')
    company = models.CharField("Назва компанії", max_length=200, default="Без компаніі")
    price = models.FloatField('Ціна')
    active = models.BooleanField('Активний', default=False, help_text="Показувати товари чи ні")
    review = RichTextField('Відгук')
    sale = models.BooleanField('Є Знижка', default=False, help_text="Покахувати є товар зі знижкою ")

    def __str__(self):
        return f'{self.name}--{self.price}'

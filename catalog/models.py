import uuid
from django.db import models
from ckeditor.fields import RichTextField


class TimeDateBaseModel:
    create = models.DateTimeField('Create', auto_now_add=True, null=True)
    update = models.DateTimeField('Update', auto_now=True, null=True)


class Tag(TimeDateBaseModel, models.Model):
    name = models.CharField("Name", max_length=30, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    tags = models.ManyToManyField(Tag, related_name='goods_tags')
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return f'{self.name}--{self.price}'


class AdditionalInfo(models.Model):
    goods = models.OneToOneField(Goods, on_delete=models.CASCADE, related_name='additional_info')
    some_field = models.CharField(max_length=100)


class OtherTag(models.Model):
    name = models.CharField("Name", max_length=30, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class GoodsOther(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='goods_other')
    other_tags = models.ManyToManyField(OtherTag, related_name='goods_other_tags')



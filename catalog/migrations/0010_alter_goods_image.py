# Generated by Django 4.2.3 on 2023-07-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_goods_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]

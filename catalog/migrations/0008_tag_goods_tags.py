# Generated by Django 4.2.3 on 2023-07-18 14:46

import catalog.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_goods_category_alter_goods_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            bases=(catalog.models.TimeDateBaseModel, models.Model),
        ),
        migrations.AddField(
            model_name='goods',
            name='tags',
            field=models.ManyToManyField(related_name='goods_tags', to='catalog.tag'),
        ),
    ]

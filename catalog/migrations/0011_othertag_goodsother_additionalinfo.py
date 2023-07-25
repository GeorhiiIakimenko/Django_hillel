# Generated by Django 4.2.3 on 2023-07-25 11:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_goods_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_other', to='catalog.goods')),
                ('other_tags', models.ManyToManyField(related_name='goods_other_tags', to='catalog.othertag')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_field', models.CharField(max_length=100)),
                ('goods', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='additional_info', to='catalog.goods')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='opening_hours',
            field=models.CharField(default=1, max_length=255, verbose_name='Время работы'),
            preserve_default=False,
        ),
    ]

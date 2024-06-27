# Generated by Django 5.0.6 on 2024-06-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_the_background_home_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('subdescription', models.TextField(max_length=255, verbose_name='Подописание')),
                ('image', models.ImageField(upload_to='image_about/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.RenameField(
            model_name='home',
            old_name='discription',
            new_name='description',
        ),
    ]

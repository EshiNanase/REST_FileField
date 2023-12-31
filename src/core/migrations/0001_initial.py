# Generated by Django 4.1.1 on 2023-06-23 21:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Файл')),
                ('processed', models.BooleanField(default=False, verbose_name='Обработан ли')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Когда загружен')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]

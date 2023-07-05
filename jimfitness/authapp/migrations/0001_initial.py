# Generated by Django 4.0.2 on 2023-07-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=12)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]

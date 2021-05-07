# Generated by Django 3.1.7 on 2021-05-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=45, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=45, verbose_name='last name')),
                ('last_update', models.DateTimeField(blank=True, max_length=45, verbose_name='last update')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actores',
                'ordering': ['first_name'],
            },
        ),
    ]
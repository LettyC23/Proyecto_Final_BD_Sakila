# Generated by Django 3.1.7 on 2021-05-13 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0003_auto_20210513_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='last_update',
            field=models.CharField(max_length=5),
        ),
    ]

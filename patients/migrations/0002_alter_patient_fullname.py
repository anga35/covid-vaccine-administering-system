# Generated by Django 4.1 on 2022-08-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='fullname',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
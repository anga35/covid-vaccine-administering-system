# Generated by Django 4.1 on 2022-08-05 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=2)),
                ('age', models.IntegerField()),
                ('health_status', models.CharField(choices=[('Healthy', 'Healthy'), ('Infected', 'Infected')], default='Infected', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(max_length=100)),
                ('sample_result', models.IntegerField()),
                ('viral_level', models.IntegerField()),
                ('test_type', models.CharField(default='Oropharyngeal', max_length=50)),
                ('test_date', models.DateTimeField(auto_now_add=True)),
                ('dosage_timeline', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
    ]
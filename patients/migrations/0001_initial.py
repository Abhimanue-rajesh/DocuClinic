# Generated by Django 5.1.1 on 2024-10-16 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_remove_operator_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.TextField(max_length=100, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3, null=True)),
                ('allergies', models.TextField(blank=True, max_length=255, null=True)),
                ('emergency_contact_name', models.CharField(max_length=100, null=True)),
                ('emergency_contact_number', models.CharField(max_length=15, null=True)),
                ('patient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_details', to='accounts.patient')),
            ],
        ),
    ]

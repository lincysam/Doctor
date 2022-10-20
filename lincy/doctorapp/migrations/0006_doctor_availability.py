# Generated by Django 4.0.5 on 2022-07-13 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0005_consultation'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_days', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('A', 'active'), ('I', 'inactive')], max_length=1, null=True)),
                ('cdate', models.DateTimeField()),
                ('mdate', models.DateTimeField()),
                ('deptid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctorapp.department')),
                ('doctorid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctorapp.user_reg')),
                ('hospitalid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctorapp.hospitallist')),
            ],
        ),
    ]
# Generated by Django 4.0.5 on 2022-07-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0007_user_reg_pword_user_reg_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='cdate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='mdate',
            field=models.DateTimeField(null=True),
        ),
    ]

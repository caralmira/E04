# Generated by Django 4.1 on 2022-10-28 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0010_alter_donationinfo_waktu_isi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationinfo',
            name='waktu_isi',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 4.1 on 2022-10-27 02:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0004_remove_donationinfo_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationinfo',
            name='waktu_isi',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
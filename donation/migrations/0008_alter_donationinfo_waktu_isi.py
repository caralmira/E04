# Generated by Django 4.1 on 2022-10-27 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0007_donationinfo_is_done_alter_donationinfo_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationinfo',
            name='waktu_isi',
            field=models.DateTimeField(blank=True, default='Fri Oct 28 06:03:17 2022'),
        ),
    ]

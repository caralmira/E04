# Generated by Django 4.1 on 2022-11-02 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0007_pengunjung_poin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengunjung',
            name='jenis_kelamin',
            field=models.CharField(choices=[('LK', 'Male'), ('PP', 'Female')], default='LK', max_length=2),
        ),
    ]

# Generated by Django 4.1 on 2022-11-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_remove_shop_type_shop_pengunjung_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='nama_baju',
            field=models.CharField(default='', max_length=255),
        ),
    ]

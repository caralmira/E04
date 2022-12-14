# Generated by Django 4.1 on 2022-10-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationinfo',
            old_name='nama_barang',
            new_name='jenis_barang',
        ),
        migrations.RemoveField(
            model_name='donationinfo',
            name='shipping_kurir',
        ),
        migrations.AlterField(
            model_name='donationinfo',
            name='amount',
            field=models.IntegerField(verbose_name='Amount (in kg)'),
        ),
        migrations.AlterField(
            model_name='donationinfo',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='donationinfo',
            name='shipping_method',
            field=models.CharField(choices=[('0', 'Antar sendiri'), ('1', 'JNE'), ('2', 'POS INDONESIA'), ('3', 'TIKI'), ('4', 'SiCepat'), ('5', 'J&T')], default=('1', 'JNE'), max_length=255, verbose_name='Metode pengiriman'),
        ),
    ]

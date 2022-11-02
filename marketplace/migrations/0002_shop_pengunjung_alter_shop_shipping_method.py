# Generated by Django 4.1 on 2022-11-02 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0008_alter_pengunjung_jenis_kelamin'),
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='pengunjung',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Authentication.pengunjung'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shipping_method',
            field=models.CharField(choices=[('JNE', 'JNE'), ('POS INDONESIA', 'POS INDONESIA'), ('TIKI', 'TIKI'), ('SiCepat', 'SiCepat'), ('J&T', 'J&T')], default=('JNE', 'JNE'), max_length=255, verbose_name='Metode pengiriman'),
        ),
    ]

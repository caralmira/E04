# Generated by Django 4.1 on 2022-10-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=50)),
                ('answer', models.TextField(blank=True)),
                ('is_answered', models.BooleanField(default = False)),
            ],
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
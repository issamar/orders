# Generated by Django 3.2.4 on 2021-08-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_commande_productype'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='qtt',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodpurchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='phone',
            field=models.IntegerField(),
        ),
    ]

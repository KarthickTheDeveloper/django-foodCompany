# Generated by Django 4.0.5 on 2022-06-24 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productionmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]

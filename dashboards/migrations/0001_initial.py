# Generated by Django 3.2.6 on 2021-08-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('category', models.CharField(choices=[('Stationery', 'Stationery'), ('Electronics', 'Electrronics'), ('Food', 'Food')], max_length=40, null=True)),
                ('quantiry', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
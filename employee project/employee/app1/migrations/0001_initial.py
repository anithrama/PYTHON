# Generated by Django 4.2.7 on 2023-12-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(max_length=25)),
                ('designation', models.CharField(max_length=45)),
                ('salary', models.IntegerField()),
                ('place', models.CharField(max_length=45)),
            ],
        ),
    ]

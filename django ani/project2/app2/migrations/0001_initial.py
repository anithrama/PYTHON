# Generated by Django 4.2.7 on 2023-11-30 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('rollno', models.IntegerField()),
                ('place', models.CharField(max_length=35)),
            ],
        ),
    ]

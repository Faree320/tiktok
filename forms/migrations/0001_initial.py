# Generated by Django 4.1 on 2022-08-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link1', models.CharField(max_length=400)),
                ('link2', models.CharField(max_length=400)),
                ('link3', models.CharField(max_length=400)),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleList', models.TextField(null=True)),
                ('descriptionsList', models.TextField(null=True)),
            ],
        ),
    ]
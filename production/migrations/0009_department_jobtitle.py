# Generated by Django 5.0.4 on 2024-04-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0008_alter_runrequest_production_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0007_production_create_date_production_production_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runrequest',
            name='production_title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
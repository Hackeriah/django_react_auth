# Generated by Django 4.2.6 on 2024-11-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_category_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.TextField(max_length=255),
        ),
    ]

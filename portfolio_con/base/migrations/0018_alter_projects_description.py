# Generated by Django 5.0.7 on 2024-07-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_projects_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

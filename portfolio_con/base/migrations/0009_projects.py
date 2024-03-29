# Generated by Django 5.0.3 on 2024-03-25 10:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Projects',
                'verbose_name_plural': 'Projeler',
            },
        ),
    ]

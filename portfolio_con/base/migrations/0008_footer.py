# Generated by Django 5.0.3 on 2024-03-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright', models.CharField(blank=True, max_length=400, null=True)),
                ('copyright_text', models.TextField(blank=True, null=True)),
                ('privacy', models.TextField(blank=True, null=True)),
                ('terms', models.TextField(blank=True, null=True)),
                ('contact', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footer',
            },
        ),
    ]
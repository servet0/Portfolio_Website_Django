# Generated by Django 5.0.7 on 2024-07-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_contactname'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ProjectName',
                'verbose_name_plural': 'Proje sayfasının altındaki yazı',
            },
        ),
    ]

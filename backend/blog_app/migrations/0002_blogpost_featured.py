# Generated by Django 4.1.3 on 2022-11-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]

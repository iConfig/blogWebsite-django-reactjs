# Generated by Django 4.1.3 on 2022-11-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_blogpost_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/2022-11-12'),
        ),
    ]

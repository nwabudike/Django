# Generated by Django 4.1 on 2022-09-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now=True),
        ),
    ]
# Generated by Django 3.1.7 on 2021-06-02 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='updated_by',
        ),
    ]

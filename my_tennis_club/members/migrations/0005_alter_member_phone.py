# Generated by Django 5.1.7 on 2025-03-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_member_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

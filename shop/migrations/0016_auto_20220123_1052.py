# Generated by Django 3.2.8 on 2022-01-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20220123_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Ratings',
        ),
        migrations.AddField(
            model_name='product',
            name='Ratings(25, 50, 75, 100)',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='cover_image_2',
            field=models.ImageField(default='', upload_to='shop/images/FeaturedImage'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_remove_tour_image_remove_tour_trending_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='main_image',
            field=models.ImageField(null=True, upload_to='places/images/'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-13 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nobele', '0013_alter_hotel_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRating',
            fields=[
                ('hotel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='nobele.hotel')),
                ('count', models.IntegerField(verbose_name='How many people voted')),
                ('summary', models.IntegerField(verbose_name='Rating summary')),
                ('key', models.IntegerField(editable=False, verbose_name='Hotel PK')),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-13 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobele', '0014_hotelrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.IntegerField(default=0, editable=False, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='hotelrating',
            name='count',
            field=models.IntegerField(default=0, verbose_name='How many people voted'),
        ),
        migrations.AlterField(
            model_name='hotelrating',
            name='summary',
            field=models.IntegerField(default=0, verbose_name='Rating summary'),
        ),
    ]

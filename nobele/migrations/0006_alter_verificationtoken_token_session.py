# Generated by Django 4.1.3 on 2022-12-10 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nobele', '0005_account_name_account_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationtoken',
            name='token',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('ip', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobele.account', unique=True)),
            ],
        ),
    ]

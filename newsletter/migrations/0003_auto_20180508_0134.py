# Generated by Django 2.0.4 on 2018-05-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20180508_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='wants_help',
            field=models.BooleanField(default=True, verbose_name='Fitness Counseling'),
        ),
    ]

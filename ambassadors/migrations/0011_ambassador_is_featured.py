# Generated by Django 2.0.4 on 2018-05-06 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambassadors', '0010_auto_20180505_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambassador',
            name='is_featured',
            field=models.BooleanField(default=True, verbose_name='Would you like them Featured?'),
        ),
    ]

# Generated by Django 2.0.4 on 2018-05-05 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambassadors', '0003_auto_20180505_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambassador',
            name='ambassador_end',
            field=models.DateField(blank=True, help_text="Leave blank if they're still an ambassador", null=True, verbose_name='Date They Were no Loner and Ambassador'),
        ),
        migrations.AddField(
            model_name='ambassador',
            name='ambassador_start',
            field=models.DateField(default=datetime.date.today, verbose_name='Date They Became an Ambassador*'),
        ),
        migrations.AddField(
            model_name='ambassador',
            name='still_an_ambassador',
            field=models.BooleanField(default=True, verbose_name='Still an Ambassador?'),
        ),
        migrations.AlterField(
            model_name='ambassador',
            name='about',
            field=models.TextField(max_length=2000, verbose_name='About*'),
        ),
        migrations.AlterField(
            model_name='ambassador',
            name='berserker_or_shieldmaiden',
            field=models.CharField(choices=[('Berserker', 'Berserker'), ('Shieldmaiden', 'Shieldmaiden')], max_length=12, verbose_name='Berserker or Shieldmaiden*?'),
        ),
        migrations.AlterField(
            model_name='ambassador',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Ambassador Name*'),
        ),
    ]
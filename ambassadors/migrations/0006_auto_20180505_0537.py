# Generated by Django 2.0.4 on 2018-05-05 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambassadors', '0005_auto_20180505_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambassador',
            name='ambassador_end',
            field=models.DateField(blank=True, help_text="Leave blank if they're still an ambassador", null=True, verbose_name='Date They Were no Longer an Ambassador'),
        ),
    ]

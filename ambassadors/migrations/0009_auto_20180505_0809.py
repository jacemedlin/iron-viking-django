# Generated by Django 2.0.4 on 2018-05-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambassadors', '0008_auto_20180505_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambassador',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Profile Picture'),
        ),
    ]

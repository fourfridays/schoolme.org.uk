# Generated by Django 2.2.9 on 2020-02-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200202_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='hero_photo_credit_link',
            field=models.URLField(blank=True, help_text='If you would like the above text to link to a website. Enter complete URL here.', null=True),
        ),
    ]

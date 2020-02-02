# Generated by Django 2.2.9 on 2020-02-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_standardpage_hero_photo_credit_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='hero_photo_credit_link',
            field=models.CharField(blank=True, help_text='If you would like the above text to link to a website. Enter complete URL here.', max_length=225, null=True),
        ),
    ]

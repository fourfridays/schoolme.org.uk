# Generated by Django 2.2.9 on 2020-02-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200119_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='hero_photo_credit_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
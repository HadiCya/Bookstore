# Generated by Django 3.2.5 on 2021-07-29 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210728_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-user_rating',), 'verbose_name_plural': 'Books'},
        ),
    ]

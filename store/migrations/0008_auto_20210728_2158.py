# Generated by Django 3.2.5 on 2021-07-29 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210728_2003'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='Unknown', max_length=255),
        ),
    ]

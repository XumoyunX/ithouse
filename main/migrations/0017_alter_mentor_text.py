# Generated by Django 5.0.7 on 2024-09-07 10:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_new_img_new_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

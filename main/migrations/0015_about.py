# Generated by Django 5.0.7 on 2024-08-30 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_mentor_text_alter_course_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos_uploaded/')),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
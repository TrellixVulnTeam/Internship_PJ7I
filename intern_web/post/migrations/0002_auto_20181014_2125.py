# Generated by Django 2.1.2 on 2018-10-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='phone',
        ),
        migrations.AddField(
            model_name='post',
            name='job_type',
            field=models.CharField(default='part', max_length=30),
            preserve_default=False,
        ),
    ]
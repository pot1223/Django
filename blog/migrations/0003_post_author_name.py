# Generated by Django 2.2.9 on 2020-01-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
    ]

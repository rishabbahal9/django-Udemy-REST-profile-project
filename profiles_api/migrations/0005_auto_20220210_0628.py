# Generated by Django 2.2 on 2022-02-10 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_auto_20220210_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilefeeditem',
            name='status_text',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]

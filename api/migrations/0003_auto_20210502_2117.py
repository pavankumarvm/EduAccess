# Generated by Django 3.1.2 on 2021-05-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210502_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='stream_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='stream_name',
            field=models.CharField(max_length=50),
        ),
    ]

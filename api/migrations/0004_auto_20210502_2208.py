# Generated by Django 3.1.2 on 2021-05-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210502_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='application',
            name='accepted_by',
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(default='N', max_length=1),
        ),
    ]

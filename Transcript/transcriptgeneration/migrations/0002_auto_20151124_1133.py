# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptgeneration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='SID',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='emailid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='yearofjoining',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='yearofpassing',
            field=models.IntegerField(default=0),
        ),
    ]

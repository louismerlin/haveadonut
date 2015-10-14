# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donuts', '0002_donut_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='donut',
            name='user',
        ),
        migrations.AddField(
            model_name='donut',
            name='chat',
            field=models.ForeignKey(to='donuts.Chat', default=0),
            preserve_default=False,
        ),
    ]

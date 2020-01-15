# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20180522_0820.py'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='redirect_url',
            field=models.CharField(help_text='An alternate URL to redirect to after form submission', max_length=200, null=True, verbose_name='Redirect url', blank=True),
        ),
    ]

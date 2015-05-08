# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='last_login',
            new_name='last_viewed_feature',
        ),
    ]

# Generated by Django 2.1.7 on 2019-07-27 13:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ports', '0003_add-field-cxx_stdlib'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='build_arch',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='submission',
            name='platform',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='submission',
            name='raw_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['os_version', 'os_arch'], name='ports_submi_os_vers_09651d_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['os_version', 'xcode_version'], name='ports_submi_os_vers_087c4f_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['build_arch'], name='ports_submi_build_a_1c8030_idx'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-24 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('larcauth', '0002_auto_20200722_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learnerpei_has_termsubjectpei',
            old_name='s13_obsersation',
            new_name='s13_observation',
        ),
        migrations.RenameField(
            model_name='learnerpei_has_termsubjectpei',
            old_name='s14_obsersation',
            new_name='s14_observation',
        ),
        migrations.RenameField(
            model_name='learnerpei_has_termsubjectpei',
            old_name='s15_obsersation',
            new_name='s15_observation',
        ),
    ]

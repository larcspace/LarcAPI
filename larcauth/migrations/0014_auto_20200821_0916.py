# Generated by Django 3.0.7 on 2020-08-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larcauth', '0013_auto_20200821_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='average_a',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='average_b',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='average_c',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='average_d',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='average_e',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='average_f',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='stddev_a',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='stddev_b',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='stddev_c',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='stddev_d',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='stddev_e',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='stddev_f',
            field=models.FloatField(null=True),
        ),
    ]

# Generated by Django 3.0.7 on 2020-08-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('larcauth', '0015_academicyear_auto_calc'),
    ]

    operations = [
        migrations.CreateModel(
            name='table_log',
            fields=[
                ('id_big', models.BigIntegerField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('log_message', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='academicyear',
            name='debug_mode',
            field=models.BooleanField(default=True),
        ),
    ]

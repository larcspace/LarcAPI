# Generated by Django 3.0.7 on 2021-05-13 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('larcauth', '0022_auto_20201224_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='API_StudentDP_has_termsubjectDP',
            fields=[
                ('learner_has_termsubject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='larcauth.learner_has_termsubject')),
                ('used', models.BooleanField(default=False)),
                ('s_name', models.CharField(max_length=72, null=True)),
                ('s_firstname', models.CharField(max_length=72, null=True)),
                ('s_pgm', models.CharField(max_length=4, null=True)),
                ('s_classroom', models.CharField(max_length=7, null=True)),
                ('s_grpm', models.CharField(max_length=44, null=True)),
                ('s_matiere', models.CharField(max_length=72, null=True)),
                ('s_teacher_name', models.CharField(max_length=72, null=True)),
                ('s_teacher_Firstname', models.CharField(max_length=72, null=True)),
                ('s_crit_a', models.CharField(max_length=72, null=True)),
                ('s_crit_b', models.CharField(max_length=72, null=True)),
                ('s_crit_c', models.CharField(max_length=72, null=True)),
                ('s_crit_d', models.CharField(max_length=72, null=True)),
                ('s_crit_e', models.CharField(max_length=72, null=True)),
                ('s_crit_f', models.CharField(max_length=72, null=True)),
                ('s_term', models.CharField(max_length=2, null=True)),
                ('f01_observation', models.CharField(max_length=360, null=True)),
                ('f02_observation', models.CharField(max_length=360, null=True)),
                ('f03_observation', models.CharField(max_length=360, null=True)),
                ('f04_observation', models.CharField(max_length=360, null=True)),
                ('f05_observation', models.CharField(max_length=360, null=True)),
                ('f06_observation', models.CharField(max_length=360, null=True)),
                ('f07_observation', models.CharField(max_length=360, null=True)),
                ('f08_observation', models.CharField(max_length=360, null=True)),
                ('f09_observation', models.CharField(max_length=360, null=True)),
                ('f10_observation', models.CharField(max_length=360, null=True)),
                ('f11_observation', models.CharField(max_length=360, null=True)),
                ('f12_observation', models.CharField(max_length=360, null=True)),
                ('f13_obsersation', models.CharField(max_length=360, null=True)),
                ('f14_obsersation', models.CharField(max_length=360, null=True)),
                ('f15_obsersation', models.CharField(max_length=360, null=True)),
                ('s01_observation', models.CharField(max_length=360, null=True)),
                ('s02_observation', models.CharField(max_length=360, null=True)),
                ('s03_observation', models.CharField(max_length=360, null=True)),
                ('s04_observation', models.CharField(max_length=360, null=True)),
                ('s05_observation', models.CharField(max_length=360, null=True)),
                ('s06_observation', models.CharField(max_length=360, null=True)),
                ('s07_observation', models.CharField(max_length=360, null=True)),
                ('s08_observation', models.CharField(max_length=360, null=True)),
                ('s09_observation', models.CharField(max_length=360, null=True)),
                ('s10_observation', models.CharField(max_length=360, null=True)),
                ('s11_observation', models.CharField(max_length=360, null=True)),
                ('s12_observation', models.CharField(max_length=360, null=True)),
                ('f01_note', models.FloatField(null=True)),
                ('f01_note_a', models.SmallIntegerField(null=True)),
                ('f01_note_b', models.SmallIntegerField(null=True)),
                ('f01_note_c', models.SmallIntegerField(null=True)),
                ('f01_note_d', models.SmallIntegerField(null=True)),
                ('f01_note_e', models.SmallIntegerField(null=True)),
                ('f01_note_f', models.SmallIntegerField(null=True)),
                ('f02_note', models.FloatField(null=True)),
                ('f02_note_a', models.SmallIntegerField(null=True)),
                ('f02_note_b', models.SmallIntegerField(null=True)),
                ('f02_note_c', models.SmallIntegerField(null=True)),
                ('f02_note_d', models.SmallIntegerField(null=True)),
                ('f02_note_e', models.SmallIntegerField(null=True)),
                ('f02_note_f', models.SmallIntegerField(null=True)),
                ('f03_note', models.FloatField(null=True)),
                ('f03_note_a', models.SmallIntegerField(null=True)),
                ('f03_note_b', models.SmallIntegerField(null=True)),
                ('f03_note_c', models.SmallIntegerField(null=True)),
                ('f03_note_d', models.SmallIntegerField(null=True)),
                ('f03_note_e', models.SmallIntegerField(null=True)),
                ('f03_note_f', models.SmallIntegerField(null=True)),
                ('f04_note', models.FloatField(null=True)),
                ('f04_note_a', models.SmallIntegerField(null=True)),
                ('f04_note_b', models.SmallIntegerField(null=True)),
                ('f04_note_c', models.SmallIntegerField(null=True)),
                ('f04_note_d', models.SmallIntegerField(null=True)),
                ('f04_note_e', models.SmallIntegerField(null=True)),
                ('f04_note_f', models.SmallIntegerField(null=True)),
                ('f05_note', models.FloatField(null=True)),
                ('f05_note_a', models.SmallIntegerField(null=True)),
                ('f05_note_b', models.SmallIntegerField(null=True)),
                ('f05_note_c', models.SmallIntegerField(null=True)),
                ('f05_note_d', models.SmallIntegerField(null=True)),
                ('f05_note_e', models.SmallIntegerField(null=True)),
                ('f05_note_f', models.SmallIntegerField(null=True)),
                ('f06_note', models.FloatField(null=True)),
                ('f06_note_a', models.SmallIntegerField(null=True)),
                ('f06_note_b', models.SmallIntegerField(null=True)),
                ('f06_note_c', models.SmallIntegerField(null=True)),
                ('f06_note_d', models.SmallIntegerField(null=True)),
                ('f06_note_e', models.SmallIntegerField(null=True)),
                ('f06_note_f', models.SmallIntegerField(null=True)),
                ('f07_note', models.FloatField(null=True)),
                ('f07_note_a', models.SmallIntegerField(null=True)),
                ('f07_note_b', models.SmallIntegerField(null=True)),
                ('f07_note_c', models.SmallIntegerField(null=True)),
                ('f07_note_d', models.SmallIntegerField(null=True)),
                ('f07_note_e', models.SmallIntegerField(null=True)),
                ('f07_note_f', models.SmallIntegerField(null=True)),
                ('f08_note', models.FloatField(null=True)),
                ('f08_note_a', models.SmallIntegerField(null=True)),
                ('f08_note_b', models.SmallIntegerField(null=True)),
                ('f08_note_c', models.SmallIntegerField(null=True)),
                ('f08_note_d', models.SmallIntegerField(null=True)),
                ('f08_note_e', models.SmallIntegerField(null=True)),
                ('f08_note_f', models.SmallIntegerField(null=True)),
                ('f09_note', models.FloatField(null=True)),
                ('f09_note_a', models.SmallIntegerField(null=True)),
                ('f09_note_b', models.SmallIntegerField(null=True)),
                ('f09_note_c', models.SmallIntegerField(null=True)),
                ('f09_note_d', models.SmallIntegerField(null=True)),
                ('f09_note_e', models.SmallIntegerField(null=True)),
                ('f09_note_f', models.SmallIntegerField(null=True)),
                ('f10_note', models.FloatField(null=True)),
                ('f10_note_a', models.SmallIntegerField(null=True)),
                ('f10_note_b', models.SmallIntegerField(null=True)),
                ('f10_note_c', models.SmallIntegerField(null=True)),
                ('f10_note_d', models.SmallIntegerField(null=True)),
                ('f10_note_e', models.SmallIntegerField(null=True)),
                ('f10_note_f', models.SmallIntegerField(null=True)),
                ('f11_note', models.FloatField(null=True)),
                ('f11_note_a', models.SmallIntegerField(null=True)),
                ('f11_note_b', models.SmallIntegerField(null=True)),
                ('f11_note_c', models.SmallIntegerField(null=True)),
                ('f11_note_d', models.SmallIntegerField(null=True)),
                ('f11_note_e', models.SmallIntegerField(null=True)),
                ('f11_note_f', models.SmallIntegerField(null=True)),
                ('f12_note', models.FloatField(null=True)),
                ('f12_note_a', models.SmallIntegerField(null=True)),
                ('f12_note_b', models.SmallIntegerField(null=True)),
                ('f12_note_c', models.SmallIntegerField(null=True)),
                ('f12_note_d', models.SmallIntegerField(null=True)),
                ('f12_note_e', models.SmallIntegerField(null=True)),
                ('f12_note_f', models.SmallIntegerField(null=True)),
                ('s01_note', models.FloatField(null=True)),
                ('s01_note_a', models.SmallIntegerField(null=True)),
                ('s01_note_b', models.SmallIntegerField(null=True)),
                ('s01_note_c', models.SmallIntegerField(null=True)),
                ('s01_note_d', models.SmallIntegerField(null=True)),
                ('s01_note_e', models.SmallIntegerField(null=True)),
                ('s01_note_f', models.SmallIntegerField(null=True)),
                ('s02_note', models.FloatField(null=True)),
                ('s02_note_a', models.SmallIntegerField(null=True)),
                ('s02_note_b', models.SmallIntegerField(null=True)),
                ('s02_note_c', models.SmallIntegerField(null=True)),
                ('s02_note_d', models.SmallIntegerField(null=True)),
                ('s02_note_e', models.SmallIntegerField(null=True)),
                ('s02_note_f', models.SmallIntegerField(null=True)),
                ('s03_note', models.FloatField(null=True)),
                ('s03_note_a', models.SmallIntegerField(null=True)),
                ('s03_note_b', models.SmallIntegerField(null=True)),
                ('s03_note_c', models.SmallIntegerField(null=True)),
                ('s03_note_d', models.SmallIntegerField(null=True)),
                ('s03_note_e', models.SmallIntegerField(null=True)),
                ('s03_note_f', models.SmallIntegerField(null=True)),
                ('s04_note', models.FloatField(null=True)),
                ('s04_note_a', models.SmallIntegerField(null=True)),
                ('s04_note_b', models.SmallIntegerField(null=True)),
                ('s04_note_c', models.SmallIntegerField(null=True)),
                ('s04_note_d', models.SmallIntegerField(null=True)),
                ('s04_note_e', models.SmallIntegerField(null=True)),
                ('s04_note_f', models.SmallIntegerField(null=True)),
                ('s05_note', models.FloatField(null=True)),
                ('s05_note_a', models.SmallIntegerField(null=True)),
                ('s05_note_b', models.SmallIntegerField(null=True)),
                ('s05_note_c', models.SmallIntegerField(null=True)),
                ('s05_note_d', models.SmallIntegerField(null=True)),
                ('s05_note_e', models.SmallIntegerField(null=True)),
                ('s05_note_f', models.SmallIntegerField(null=True)),
                ('s06_note', models.FloatField(null=True)),
                ('s06_note_a', models.SmallIntegerField(null=True)),
                ('s06_note_b', models.SmallIntegerField(null=True)),
                ('s06_note_c', models.SmallIntegerField(null=True)),
                ('s06_note_d', models.SmallIntegerField(null=True)),
                ('s06_note_e', models.SmallIntegerField(null=True)),
                ('s06_note_f', models.SmallIntegerField(null=True)),
                ('s07_note', models.FloatField(null=True)),
                ('s07_note_a', models.SmallIntegerField(null=True)),
                ('s07_note_b', models.SmallIntegerField(null=True)),
                ('s07_note_c', models.SmallIntegerField(null=True)),
                ('s07_note_d', models.SmallIntegerField(null=True)),
                ('s07_note_e', models.SmallIntegerField(null=True)),
                ('s07_note_f', models.SmallIntegerField(null=True)),
                ('s08_note', models.FloatField(null=True)),
                ('s08_note_a', models.SmallIntegerField(null=True)),
                ('s08_note_b', models.SmallIntegerField(null=True)),
                ('s08_note_c', models.SmallIntegerField(null=True)),
                ('s08_note_d', models.SmallIntegerField(null=True)),
                ('s08_note_e', models.SmallIntegerField(null=True)),
                ('s08_note_f', models.SmallIntegerField(null=True)),
                ('s09_note', models.FloatField(null=True)),
                ('s09_note_a', models.SmallIntegerField(null=True)),
                ('s09_note_b', models.SmallIntegerField(null=True)),
                ('s09_note_c', models.SmallIntegerField(null=True)),
                ('s09_note_d', models.SmallIntegerField(null=True)),
                ('s09_note_e', models.SmallIntegerField(null=True)),
                ('s09_note_f', models.SmallIntegerField(null=True)),
                ('s10_note', models.FloatField(null=True)),
                ('s10_note_a', models.SmallIntegerField(null=True)),
                ('s10_note_b', models.SmallIntegerField(null=True)),
                ('s10_note_c', models.SmallIntegerField(null=True)),
                ('s10_note_d', models.SmallIntegerField(null=True)),
                ('s10_note_e', models.SmallIntegerField(null=True)),
                ('s10_note_f', models.SmallIntegerField(null=True)),
                ('s11_note', models.FloatField(null=True)),
                ('s11_note_a', models.SmallIntegerField(null=True)),
                ('s11_note_b', models.SmallIntegerField(null=True)),
                ('s11_note_c', models.SmallIntegerField(null=True)),
                ('s11_note_d', models.SmallIntegerField(null=True)),
                ('s11_note_e', models.SmallIntegerField(null=True)),
                ('s11_note_f', models.SmallIntegerField(null=True)),
                ('s12_note', models.FloatField(null=True)),
                ('s12_note_a', models.SmallIntegerField(null=True)),
                ('s12_note_b', models.SmallIntegerField(null=True)),
                ('s12_note_c', models.SmallIntegerField(null=True)),
                ('s12_note_d', models.SmallIntegerField(null=True)),
                ('s12_note_e', models.SmallIntegerField(null=True)),
                ('s12_note_f', models.SmallIntegerField(null=True)),
                ('s13_note', models.FloatField(null=True)),
                ('s13_note_a', models.SmallIntegerField(null=True)),
                ('s13_note_b', models.SmallIntegerField(null=True)),
                ('s13_note_c', models.SmallIntegerField(null=True)),
                ('s13_note_d', models.SmallIntegerField(null=True)),
                ('s13_note_e', models.SmallIntegerField(null=True)),
                ('s13_note_f', models.SmallIntegerField(null=True)),
                ('s13_observation', models.CharField(max_length=720, null=True)),
                ('s14_note', models.FloatField(null=True)),
                ('s14_note_a', models.SmallIntegerField(null=True)),
                ('s14_note_b', models.SmallIntegerField(null=True)),
                ('s14_note_c', models.SmallIntegerField(null=True)),
                ('s14_note_d', models.SmallIntegerField(null=True)),
                ('s14_note_e', models.SmallIntegerField(null=True)),
                ('s14_note_f', models.SmallIntegerField(null=True)),
                ('s14_observation', models.CharField(max_length=360, null=True)),
                ('s15_note', models.FloatField(null=True)),
                ('s15_note_a', models.SmallIntegerField(null=True)),
                ('s15_note_b', models.SmallIntegerField(null=True)),
                ('s15_note_c', models.SmallIntegerField(null=True)),
                ('s15_note_d', models.SmallIntegerField(null=True)),
                ('s15_note_e', models.SmallIntegerField(null=True)),
                ('s15_note_f', models.SmallIntegerField(null=True)),
                ('s15_observation', models.CharField(max_length=1200, null=True)),
                ('cp_note', models.FloatField(null=True)),
                ('cp_note_a', models.SmallIntegerField(null=True)),
                ('cp_note_b', models.SmallIntegerField(null=True)),
                ('cp_note_c', models.SmallIntegerField(null=True)),
                ('cp_note_d', models.SmallIntegerField(null=True)),
                ('cp_note_e', models.SmallIntegerField(null=True)),
                ('cp_note_f', models.SmallIntegerField(null=True)),
                ('cp_observation', models.CharField(max_length=360, null=True)),
                ('jgt_a', models.SmallIntegerField(null=True)),
                ('jgt_b', models.SmallIntegerField(null=True)),
                ('jgt_c', models.SmallIntegerField(null=True)),
                ('jgt_d', models.SmallIntegerField(null=True)),
                ('jgt_e', models.SmallIntegerField(null=True)),
                ('jgt_f', models.SmallIntegerField(null=True)),
                ('jgt_obsersation', models.CharField(max_length=1200, null=True)),
                ('ei_note', models.FloatField(null=True)),
                ('ei_observation', models.CharField(max_length=2000, null=True)),
                ('ei_objectif', models.CharField(max_length=250, null=True)),
                ('cpei', models.FloatField(null=True)),
                ('cc_on_20', models.FloatField(null=True)),
                ('moy_on_20', models.FloatField(null=True)),
                ('moy_on_7', models.FloatField(null=True)),
                ('bacblanc_v', models.FloatField(null=True)),
                ('bacblanc', models.SmallIntegerField(null=True)),
                ('term_observation', models.TextField(null=True)),
            ],
            bases=('larcauth.learner_has_termsubject',),
        ),
    ]

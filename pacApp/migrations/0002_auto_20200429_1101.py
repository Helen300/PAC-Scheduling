# Generated by Django 3.0.4 on 2020-04-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adrequest',
            name='rank_1',
        ),
        migrations.RemoveField(
            model_name='adrequest',
            name='rank_2',
        ),
        migrations.RemoveField(
            model_name='adrequest',
            name='rank_3',
        ),
        migrations.RemoveField(
            model_name='adrequest',
            name='rank_4',
        ),
        migrations.RemoveField(
            model_name='adrequest',
            name='rank_5',
        ),
        migrations.AddField(
            model_name='adrequest',
            name='bloomberg_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adrequest',
            name='dillon_dance_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adrequest',
            name='dillon_mar_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adrequest',
            name='dillon_mpr_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adrequest',
            name='murphy_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adrequest',
            name='ns_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adrequest',
            name='ns_theatre_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adrequest',
            name='ns_warmup_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adrequest',
            name='whitman_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adrequest',
            name='wilcox_rank',
            field=models.IntegerField(default=0),
        ),
    ]

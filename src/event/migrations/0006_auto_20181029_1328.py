# Generated by Django 2.1.2 on 2018-10-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20181014_1225'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='event_provi_name_d8b28e_idx'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['name'], name='event_provi_name_f1a6c7_idx'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['min_ticket_price'], name='event_provi_min_tic_391444_idx'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['max_ticket_price'], name='event_provi_max_tic_d0eb1a_idx'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['start_time'], name='event_provi_start_t_44630f_idx'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['finish_time'], name='event_provi_finish__3a9d62_idx'),
        ),
        migrations.AddIndex(
            model_name='organizer',
            index=models.Index(fields=['name'], name='event_provi_name_8c8fe8_idx'),
        ),
    ]

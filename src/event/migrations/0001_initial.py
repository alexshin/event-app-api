# Generated by Django 2.1.2 on 2018-10-13 14:34

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('provider_object_id', models.CharField(max_length=60, verbose_name="Provider's object id")),
                ('provider', models.PositiveSmallIntegerField(choices=[(1, 'Eventbrite')], verbose_name='Provider')),
                ('is_actual', models.BooleanField(default=False, verbose_name='Is actual')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'event_provider_category',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('provider_object_id', models.CharField(max_length=60, verbose_name="Provider's object id")),
                ('provider', models.PositiveSmallIntegerField(choices=[(1, 'Eventbrite')], verbose_name='Provider')),
                ('is_actual', models.BooleanField(default=False, verbose_name='Is actual')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('uri', models.URLField(blank=True, verbose_name='URL')),
                ('description_plain', models.TextField(blank=True, help_text='plain text', verbose_name='Description (text)')),
                ('description_html', models.TextField(blank=True, help_text='html', verbose_name='Organizer description')),
                ('start_time', models.DateTimeField(null=True, verbose_name='Start time')),
                ('finish_time', models.DateTimeField(null=True, verbose_name='Finish time')),
                ('ticket_price_currency', models.CharField(max_length=3, verbose_name='Currency')),
                ('min_ticket_price', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='Minimum ticket price')),
                ('max_ticket_price', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='Maximum ticket price')),
                ('changed_by_provider_hash', models.CharField(max_length=32, null=True, verbose_name='Changed by provider hash')),
                ('provider_specific_data', django.contrib.postgres.fields.jsonb.JSONField(null=True, verbose_name='Provider specific data')),
                ('logo_uri', models.URLField(blank=True, verbose_name='Logo URI')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'event',
                'db_table': 'event_provider_event',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('provider_object_id', models.CharField(max_length=60, verbose_name="Provider's object id")),
                ('provider', models.PositiveSmallIntegerField(choices=[(1, 'Eventbrite')], verbose_name='Provider')),
                ('is_actual', models.BooleanField(default=False, verbose_name='Is actual')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('uri', models.URLField(blank=True, verbose_name='URL')),
                ('description_plain', models.TextField(blank=True, help_text='plain text', verbose_name='Description (text)')),
                ('description_html', models.TextField(blank=True, help_text='html', verbose_name='Organizer description')),
                ('logo_uri', models.URLField(blank=True, verbose_name='Logo URI')),
            ],
            options={
                'verbose_name': 'organizer',
                'verbose_name_plural': 'organizer',
                'db_table': 'event_provider_organizer',
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='organizer',
            index=models.Index(fields=['provider', 'is_actual'], name='event_provi_provide_94796a_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='organizer',
            unique_together={('id', 'provider_object_id')},
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Category'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Organizer'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['provider', 'is_actual'], name='event_provi_provide_adf319_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('id', 'provider_object_id'), ('provider', 'name')},
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['provider', 'is_actual'], name='event_provi_provide_669b3f_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('id', 'provider_object_id')},
        ),
    ]

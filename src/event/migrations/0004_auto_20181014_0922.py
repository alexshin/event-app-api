# Generated by Django 2.1.2 on 2018-10-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20181014_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description_html',
            field=models.TextField(blank=True, help_text='html', null=True, verbose_name='Organizer description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description_plain',
            field=models.TextField(blank=True, help_text='plain text', null=True, verbose_name='Description (text)'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='description_html',
            field=models.TextField(blank=True, help_text='html', null=True, verbose_name='Organizer description'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='description_plain',
            field=models.TextField(blank=True, help_text='plain text', null=True, verbose_name='Description (text)'),
        ),
    ]

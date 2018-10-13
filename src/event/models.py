from django.contrib.postgres.fields import JSONField
from django.db import models
from .providers.settings import EVENT_PROVIDERS

from utils.model_mixings import TimestampMixin


class ProviderMixin(TimestampMixin, models.Model):
    provider_object_id = models.CharField('Provider\'s object id', blank=False, max_length=60)
    provider = models.PositiveSmallIntegerField('Provider', blank=False, null=False, choices=EVENT_PROVIDERS)

    #  This field is used by the updating process. Before updating, all rows of provider set to is_actual=False
    #  It's not production ready but good enough for this testing project
    is_actual = models.BooleanField('Is actual', null=False, default=False)

    class Meta:
        unique_together = ('id', 'provider_object_id')
        indexes = [
            models.Index(fields=['provider', 'is_actual'])
        ]
        abstract = True


class Category(ProviderMixin, models.Model):
    name = models.CharField('Name', max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta(ProviderMixin.Meta):
        db_table = 'event_provider_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        unique_together = [
            ('provider', 'name'),
            ProviderMixin.Meta.unique_together
        ]


class Organizer(ProviderMixin, models.Model):
    name = models.CharField('Name', max_length=255, blank=False)
    uri = models.URLField('URL', blank=True)

    description_plain = models.TextField('Description (text)', blank=True, help_text='plain text')
    description_html = models.TextField('Organizer description', blank=True, help_text='html')

    logo_uri = models.URLField('Logo URI', blank=True)

    @property
    def description(self):
        if len(self.description_html) > 0:
            return self.description_html
        return self.description_plain

    def __str__(self):
        return self.name

    class Meta(ProviderMixin.Meta):
        db_table = 'event_provider_organizer'
        verbose_name = 'organizer'
        verbose_name_plural = 'organizer'


class Event(ProviderMixin, models.Model):
    name = models.CharField('Name', max_length=255, blank=False)
    uri = models.URLField('URL', blank=True)

    description_plain = models.TextField('Description (text)', blank=True, help_text='plain text')
    description_html = models.TextField('Organizer description', blank=True, help_text='html')

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    organizer = models.ForeignKey(Organizer, null=False, on_delete=models.CASCADE)

    start_time = models.DateTimeField('Start time', null=True)
    finish_time = models.DateTimeField('Finish time', null=True)

    ticket_price_currency = models.CharField('Currency', max_length=3)
    min_ticket_price = models.DecimalField('Minimum ticket price', decimal_places=4, max_digits=12)
    max_ticket_price = models.DecimalField('Maximum ticket price', decimal_places=4, max_digits=12)

    changed_by_provider_hash = models.CharField('Changed by provider hash', null=True, max_length=32)  # md5 hash

    provider_specific_data = JSONField('Provider specific data', null=True)

    logo_uri = models.URLField('Logo URI', blank=True)

    @property
    def description(self):
        if len(self.description_html) > 0:
            return self.description_html
        return self.description_plain

    def __str__(self):
        return self.name

    class Meta(ProviderMixin.Meta):
        db_table = 'event_provider_event'
        verbose_name = 'event'
        verbose_name_plural = 'event'

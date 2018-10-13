from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TimestampMixin(models.Model):
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        abstract = True


class OwnerMixin(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True


class OwnerOrNullMixin(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

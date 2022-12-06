import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Auth0User(TimeStampedModel):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4)
    sub = models.TextField()

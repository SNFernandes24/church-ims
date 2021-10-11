from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.urls import reverse

from .constants import GENDER_CHOICES
from .utils import get_age, get_age_category
from .validators import validate_full_name


class Person(models.Model):
    username = models.CharField(
        max_length=50, unique=True, validators=[UnicodeUsernameValidator()]
    )
    full_name = models.CharField(max_length=300, validators=[validate_full_name])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(verbose_name="date of birth")
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        help_text="The user who created this record.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:  # noqa
        ordering = ["username"]
        verbose_name_plural = "people"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("people:person_detail", kwargs={"username": self.username})

    @property
    def age(self):
        return get_age(self.dob)

    @property
    def age_category(self):
        return get_age_category(self.age)

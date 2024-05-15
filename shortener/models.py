from django.contrib import messages
from django.db import models
import validators
import random
import string


# Create your models here.
class UrlShortener(models.Model):
    complete_url = models.CharField(max_length=300, unique=True, null=False)
    short_url = models.CharField(max_length=5, unique=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    visits = models.PositiveIntegerField(default=0)

    def increase_visit(self):
        self.visits = self.visits + 1
        self.save()

    @staticmethod
    def random_characters():
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        short_url = ''.join(random.choice(letters) for letter in range(5))

        return short_url

    @classmethod
    def shorten_url(cls):
        short_url = cls.random_characters()

        if cls.invalid_short_url(short_url):
            short_url = cls.random_characters()

        return short_url

    @classmethod
    def complete_url_exist(cls, complete_url):
        return cls.objects.filter(complete_url=complete_url).exists()

    @staticmethod
    def invalid_complete_url(complete_url):
        return not validators.url(complete_url)

    @classmethod
    def complete_url_errors(cls, request, complete_url):
        if cls.complete_url_exist(complete_url):
            messages.error(request, "The Url Already Exist", extra_tags="complete_url_exist")

        if cls.invalid_complete_url(complete_url):
            messages.error(request, "The Url Is Invalid", extra_tags="complete_url_invalid")

        return cls.complete_url_exist(complete_url) or cls.invalid_complete_url(complete_url)

    @classmethod
    def invalid_short_url(cls, short_url):
        return not cls.objects.filter(short_url=short_url).exists()

    def __str__(self):
        return f"Complete: {self.complete_url} - Short: {self.short_url}"

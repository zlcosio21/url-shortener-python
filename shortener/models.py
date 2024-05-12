from django.db import models
from django.contrib import messages
import random
import string
import validators

# Create your models here.
class UrlShortener(models.Model):
    complete_url = models.CharField(max_length=300, unique=True, null=False)
    short_url = models.CharField(max_length=5, unique=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    visits = models.PositiveIntegerField(default=0)

    def increase_visit(self):
        self.visits = self.visits + 1
        self.save()

    def shorten_url():
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        short_url = ''.join(random.choice(letters) for letter in range(5))

        if UrlShortener.objects.filter(short_url=short_url).exists():
            short_url = ''.join(random.choice(letters) for letter in range(5))

        return short_url

    def complete_url_errors(request, complete_url):
        complete_url_exist = UrlShortener.objects.filter(complete_url=complete_url).exists()
        complete_url_invalid = not validators.url(complete_url)

        if complete_url_exist:
            messages.error(request, "The Url Already Exist", extra_tags="complete_url_exist")

        if complete_url_invalid:
            messages.error(request, "The Url Is Invalid", extra_tags="complete_url_invalid")

        return complete_url_exist or complete_url_invalid

    def invalid_url(request, short_url):
        return not UrlShortener.objects.filter(short_url=short_url).exists()

    def __str__(self):
        return f"Complete: {self.complete_url} - Short: {self.short_url}"

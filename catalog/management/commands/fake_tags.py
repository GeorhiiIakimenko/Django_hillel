import random
from django.core.management.base import BaseCommand
from catalog.models import Tag
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Create fake tags'

    def handle(self, *args, **kwargs):
        for _ in range(5):
            Tag.objects.create(name=fake.words())

        print("New tags create")
import uuid
import random
from django.core.management.base import BaseCommand
from catalog.models import Goods, Category, Tag
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Create fake goods'

    def handle(self, *args, **kwargs):
        for _ in range(5):
            goods = Goods.objects.create(
                name=fake.company(),
                description=fake.text(),
                company=fake.company(),
                price=random.uniform(10, 1000),
                active=fake.boolean(),
                review=fake.text(),
                sale=fake.boolean(),
                category=Category.objects.first(),
            )
            goods.tags.set(Tag.objects.all()[:3])


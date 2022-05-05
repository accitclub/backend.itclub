import random

from factory import Faker
from factory.django import DjangoModelFactory
from itc_backend.apps.core.models.executive import ExecutiveYear, Executive, SocialMedia


class SocialMediaFactory(DjangoModelFactory):
    name = Faker("name")
    link = Faker("name")

    class Meta:
        model = SocialMedia


class ExecutivesFactory(DjangoModelFactory):
    name = Faker("name")
    post = Faker("job")
    serial = random.randrange(1, 10)
    executive_year = None

    class Meta:
        model = Executive


class ExecutiveYearFactory(DjangoModelFactory):
    title = Faker("name")
    year = Faker("name")

    class Meta:
        model = ExecutiveYear

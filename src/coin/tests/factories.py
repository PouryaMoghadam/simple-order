import factory
from faker import Faker

from ..models import Coin

fake = Faker()


class CoinFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Coin

    name = factory.LazyAttribute(lambda _: fake.currency_name())
    symbol = factory.LazyAttribute(lambda _: fake.currency_code())
    last_price = factory.LazyAttribute(
        lambda _: fake.pydecimal(left_digits=10, right_digits=2, positive=True)
    )

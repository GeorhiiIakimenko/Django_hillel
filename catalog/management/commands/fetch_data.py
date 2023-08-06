from django.core.management.base import BaseCommand
import requests
from catalog.models import CryptoCurrency
from django.utils import timezone


class Command(BaseCommand):
    help = 'Fetches data from the API and saves it to the CryptoCurrency model'

    def handle(self, *args, **options):
        url = 'https://api.binance.com/api/v3/ticker/price'
        symbols = [
            'BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'BCHUSDT',
            'LTCUSDT', 'LINKUSDT', 'DOTUSDT', 'ADAUSDT', 'XLMUSDT',
        ]
        bulk_create_data = []

        for symbol in symbols:
            response = requests.get(url, params={'symbol': symbol})
            data = response.json()
            name = symbol[:-4]
            price = data.get('price')
            last_updated = timezone.now().replace(tzinfo=None)

            # Prepare data for bulk create
            bulk_create_data.append(
                CryptoCurrency(
                    name=name,
                    symbol=symbol,
                    price=price,
                    last_updated=last_updated
                )
            )
            self.stdout.write(f'Successfully fetched data for {name}')


        CryptoCurrency.objects.bulk_create(bulk_create_data)
        self.stdout.write(self.style.SUCCESS('Successfully saved data using bulk create'))


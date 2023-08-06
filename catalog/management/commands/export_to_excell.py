# crypto_app/management/commands/export_to_excel.py
from django.core.management.base import BaseCommand
import openpyxl
from catalog.models import CryptoCurrency
from django.utils import timezone


class Command(BaseCommand):
    help = 'Exports data from the CryptoCurrency model to an Excel file'

    def handle(self, *args, **options):
        file_name = 'crypto_data.xlsx'
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Name', 'Symbol', 'Price', 'Last Updated'])
        crypto_currencies = CryptoCurrency.objects.all()
        for crypto_currency in crypto_currencies:
            last_updated = crypto_currency.last_updated.replace(tzinfo=None)
            ws.append([crypto_currency.name, crypto_currency.symbol, crypto_currency.price, last_updated])
        wb.save(file_name)
        self.stdout.write(f'Successfully exported data to {file_name}')

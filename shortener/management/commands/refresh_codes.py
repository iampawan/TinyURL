from django.core.management.base import BaseCommand, CommandError
from shortener.models import FurrURL


class Command(BaseCommand):
    help = 'Refresh all FurrURL Shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)


    def handle(self, *args, **options):
        return FurrURL.objects.refresh_shortcodes(items=options['items'])
        
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command tells you that he loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you I love you"
        )

    def handle(self, *args, **options):
        print(args, options)
        print("i love you ")

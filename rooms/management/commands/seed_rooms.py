import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms.models import Room
from rooms.models import RoomType
from users.models import User


class Command(BaseCommand):

    help = "This command creates many rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=5,
            type=int,
            help="How many rooms do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        all_room_types = RoomType.objects.all()
        seeder.add_entity(
            Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_room_types),
                "guests": lambda x: random.randint(5, 15),
                "price": lambda x: random.randint(100, 500),
                "beds": lambda x: random.randint(1, 10),
                "bedrooms": lambda x: random.randint(1, 10),
                "baths": lambda x: random.randint(1, 10),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created."))

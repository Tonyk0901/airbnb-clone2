import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms.models import Room, Photo, RoomType, Amenity, HouseRule, Facility
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
        created_rooms = flatten(list(seeder.execute().values()))
        amenities = Amenity.objects.all()
        facilities = Facility.objects.all()
        house_rules = HouseRule.objects.all()
        for keys in created_rooms:
            room = Room.objects.get(pk=keys)
            for i in range(
                3, random.randint(10, 30)
            ):  # Procedure to add photos to rooms
                Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )

            for a in amenities:  # Procedure to add amenities to rooms
                random_number = random.randint(0, 10)
                if random_number % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:  # Procedure to add facilities to rooms
                random_number = random.randint(0, 10)
                if random_number % 2 == 0:
                    room.facilities.add(f)

            for h in house_rules:  # Procedure to add house rules to rooms
                random_number = random.randint(0, 10)
                if random_number % 2 == 0:
                    room.house_rules.add(h)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created."))

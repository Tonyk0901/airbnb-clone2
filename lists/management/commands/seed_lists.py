import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists.models import List
from users.models import User
from rooms.models import Room


class Command(BaseCommand):

    help = "This command creates many reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=5,
            type=int,
            help="How many lists do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(
            List, number, {"user": lambda x: random.choice(users),},
        )
        created_lists = flatten(list(seeder.execute().values()))
        for keys in created_lists:
            Lists = List.objects.get(pk=keys)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            Lists.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{number} reviews created."))

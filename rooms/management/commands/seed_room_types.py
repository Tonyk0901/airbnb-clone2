from django.core.management.base import BaseCommand
from rooms import models as room_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        room_types = [
            "Entire place",
            "Private room",
            "Hotel room",
            "Shared room",
        ]
        for r in room_types:
            room_model.RoomType.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS("4 Room_Type created."))

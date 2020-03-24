from django.core.management.base import BaseCommand
from rooms import models as room_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        house_rules = [
            "No Parties",
            "No Unregistered Guest",
            "No Smoking",
            "No Pets",
            "No Exception To Check-In and Check-Out Times Unless Discussed With The Host In Advance",
            "Clean Your Dirty Dishes Before Check-Out or You Will Charged A Fee",
            "Guests Should Dispose Of The Garbage In The Trash Can",
            "No Shoes Inside The Home Please",
        ]
        for h in house_rules:
            room_model.HouseRule.objects.create(name=h)
        self.stdout.write(self.style.SUCCESS("8 house rules created."))

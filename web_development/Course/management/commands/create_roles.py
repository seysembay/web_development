from django.core.management import BaseCommand
from User.models import Role
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            roles = [
                {'id': 1, 'name': 'teacher'},
                {'id': 2, 'name': 'student'},
            ]

            for role in roles:
                Role.objects.create(**role)
        except IntegrityError:
            self.stdout.write(
                self.style.SUCCESS('Already Exists')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Done')
            )

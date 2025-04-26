from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create a superuser with predefined credentials'

    def handle(self, *args, **options):
        username = os.environ.get('SUPER_USERNAME', 'admin')
        email = os.environ.get('SUPER_EMAIL', 'test@test.com')
        password = os.environ.get('SUPER_PASSWORD','password123')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username,email,password)
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))

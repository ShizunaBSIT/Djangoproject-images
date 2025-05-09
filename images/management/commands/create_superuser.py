from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username= os.getenv('SUPER_USERNAME', 'admin'),
                password= os.getenv('SUPER_PASSWORD','complexpassword123')
            )
            print('Superuser has been created')

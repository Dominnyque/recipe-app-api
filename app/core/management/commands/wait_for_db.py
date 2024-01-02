"""
Django command to wait for the database to be available before string app
"""
import time

from psycopg2 import OperationalError as Psycopg2opError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Entrypoint to command."""
        self.stdout.write("Waiting for database")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (Psycopg2opError, OperationalError):
                self.stdout.write(" database is not available, wait 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!')),

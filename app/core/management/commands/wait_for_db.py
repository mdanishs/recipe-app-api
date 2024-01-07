"""
Django cmd to wait for db to be available
"""
from time import sleep

from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

class Command(BaseCommand):
  
  def handle(self, *args, **options):
    self.stdout.write('Waiting for db')
    db_up = False
    while db_up is False:
      try:
        self.check(databases=['default'])
        db_up = True
      except (Psycopg2Error, OperationalError) as e:
        print(e)
        self.stdout.write('NA waiting 1 sec')
        sleep(1)

    self.stdout.write(self.style.SUCCESS('Database available!'))
    


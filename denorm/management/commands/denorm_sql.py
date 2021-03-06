"""
Prints out the SQL used to create all triggers needed to track changes
to models that may cause data to become inconsistent.
"""
from django.core.management.base import BaseCommand
from denorm import denorms

class Command(BaseCommand):

    def handle(self, **kwargs):
        triggerset = denorms.build_triggerset()
        print '\n'.join((trigger.sql() for name,trigger in triggerset.triggers.iteritems()))


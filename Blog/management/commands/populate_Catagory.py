from typing import Any

from django.db.models import Model
from django.core.management.base import BaseCommand

from Blog.models import Catagory

class Command(BaseCommand):

    help = "this command inserts post data"

    def handle(self, *args:Any, **options:Any):

        # deleting existing data
        Catagory.objects.all().delete()

        catagories = ['Sports','Technologies','Science','Art','Food']



        for catagory_name in catagories:
            Catagory.objects.create(name = catagory_name)

        self.stdout.write(self.style.SUCCESS("Completed Inserting Data"))
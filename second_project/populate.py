import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'second_project.settings')

import django
django.setup()

from secondapp.models import Userinfo
from faker import Faker
fakegen=Faker()

def population(N=5):


    for entry in range(N):
        fake_name=fakegen.name().split()
        fake_firstname=fake_name[0]
        fake_lastname=fake_name[1]
        fake_email=fakegen.email()

        user=Userinfo.objects.get_or_create(firstname=fake_firstname,lastname=fake_lastname,email=fake_email)[0]


if __name__ == '__main__':
    print("Creating Database")
    population(50)
    print("Successfully created Database")

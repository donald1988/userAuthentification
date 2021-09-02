from django.db.models.signals import post_save
from . models import Customer
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name = 'customer')
        instance.user.groups.add(group)
        Customer.objects.create(user = instance, name = instance.username,)

        print('profile was created')

post_save.connect(customer_profile, sender = User)
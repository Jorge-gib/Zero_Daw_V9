# your_app_name/management/commands/initialize_permissions.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission

class Command(BaseCommand):
    help = 'Initialize groups and permissions'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Usuarios')
        if created:
            permissions = ['add_user', 'change_user', 'delete_user', 'view_user']
            for perm in permissions:
                permission = Permission.objects.get(codename=perm)
                group.permissions.add(permission)

        try:
            user = User.objects.get(username='alberto@gmail.com')
            user.groups.add(group)
            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully initialized groups and permissions'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User does not exist'))

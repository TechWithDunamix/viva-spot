from tortoise import manager

class Manager(manager.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
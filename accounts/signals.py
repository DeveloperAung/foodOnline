from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from . models import User, UserProfile


# This is for using Signals # This is receiver # User is sender
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    # print('created')
    if created:
        UserProfile.objects.create(user=instance)
        # print('User profile is created')
    else:
        try:
            profile =  UserProfile.objects.get(user=instance)
            profile.save()
            # print('User is updated')
        except:
            UserProfile.objects.create(user=instance)
            # Create user profile is not exist


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    # print(instance.username, 'This user have been save')
    pass
# post_save.connect(post_save_create_profile_receiver,)
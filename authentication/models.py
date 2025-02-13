from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

	phone = models.CharField(max_length = 50, null=True, verbose_name="Телефон")
	addres = models.CharField(max_length=200, blank=True, verbose_name="Город")

	class Meta():
		verbose_name_plural = "Профиль пользователя"

	def __str__(self):
		return f'{self.user.username} -- {self.phone}'


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()







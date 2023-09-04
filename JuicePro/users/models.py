import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
####################### User manager saugantis userio email ir password ###########################
class UserManager(BaseUserManager):
    # funkcija kuri sukuria useri
    def create_user(self, email, password):
        user = self.model(email=email, password=password)

        user.set_password(password)
        user.save(using=self._db)
        return user
    # funkcija kuri sukuria superuseri
    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        # kvieciame create_user funkcija per argumenta paduodame email ir password
        user.is_staff = True # gali jungtis prie admin panel
        user.is_admin = True
        user.is_employee = True
        user.save(using=self._db)
        return user

####################### User registracija su uuid ###########################
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, blank=True, null=True)
    objects = UserManager()
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    #  kodas kuris suteikia adminui visus leidimus ir leidzia adminui prieiti prie visu objektu
    def has_module_perms(self, app_label):
        return self.is_admin
    # kodas kuris suteikia adminui visus leidimus ir leidzia adminui prieiti prie visu moduliu

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

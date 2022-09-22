from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from core.models import TimeStampModel

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, nickname, email, password, **kwargs):
        if not email:
            raise ValueError('email must be needed')

        user = self.model(nickname, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, TimeStampModel):
    email    = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    company  = models.ForeignKey('recruits.Company', on_delete=models.CASCADE)
    
    objects  = UserManager()
    
    USERNAME_FIELD  = 'nickname'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'users'
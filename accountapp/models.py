from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError('must have user email')
        if not username:
            raise ValueError('must have user username')
        if not name:
            raise ValueError('must have user name')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, email, username, name, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
            name=name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    username = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'username'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.username


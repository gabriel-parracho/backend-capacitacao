from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=10, unique=True)
    is_admin = models.BooleanField() 
    #isso serve pra atribuir um "cargo" ao usuario, no caso de vários cargos, pode colocar vários tipos com false,false,false,true, por exemplo
    join_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
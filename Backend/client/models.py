import re

from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from utils.cpf_validator import cpf_validator


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')  # noqa: E501
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    address = models.CharField(max_length=50, verbose_name='Endereço')
    number = models.CharField(max_length=5, verbose_name='Numero')
    complement = models.CharField(max_length=30, verbose_name='Complemento')
    area = models.CharField(max_length=30, verbose_name='Bairro')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    city = models.CharField(max_length=30, verbose_name='Cidade')
    state = models.CharField(
        default='SP',
        max_length=2,
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def clean(self):
        error_messages = {}

        if not cpf_validator(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido.'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'CEP invalido, digite os 8 digitos do CEP'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

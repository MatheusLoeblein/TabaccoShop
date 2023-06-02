from django.test import TestCase

from utils.cpf_validator import cpf_validator


class CpfValidatorTest(TestCase):
    def test_false_cpf_validador(self):
        self.assertFalse(cpf_validator('11111111111'))

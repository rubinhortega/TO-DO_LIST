from django.test import TestCase

""""""
# Create your tests here.
from .models import To_do_listModel
from datetime import datetime
class To_do_listModelTest(TestCase):
    def setUp(self):
        self.to_do_list = 'Atividade'
        self.mes = 05
        self.dia = 05
        self.ano = 23
        self.cadastro = To_do_listModel(
        nome=self.atividade,
        dia=self.dia,
        mes=self.mes,
)
        self.cadastro.save()
        
    def test_created(self):
        self.assertTrue(To_do_listModel.objects.exists())
    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)
    def test_nome_atividade(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.atividade)
    def test_dia_atividade(self):
        dia = self.cadastro.__dict__.get('dia', '')
        ano = self.cadastro.__dict__.get('ano', '')
        self.assertEqual(dia, self.dia)
""""""
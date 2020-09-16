from django.db import models
"""from equipe.models import Equipe
from usuario.models import Usuario
from posts.models import Post
from projetos.models import Projeto"""

class Organizacao(models.Model):
    org_id = models.AutoField(primary_key=True)
    org_nome = models.CharField("Nome", max_length=50,null=False, blank=False)
    org_fundacao = models.DateField("Fundação")
    org_cidade = models.CharField("Cidade",max_length=50,null=False, blank=False)
    org_estado = models.CharField("Estado (UF)",max_length=2,null=False, blank=False)
    org_area = models.CharField("Area de Atuação",max_length=20,null=False, blank=False)
    org_email = models.EmailField(max_length=254)
    org_telefone = models.IntegerField(null=False, blank=False)
    org_senha = models.CharField(max_length=100,null=False, blank=False)
    org_avatar = models.ImageField(upload_to=None, height_field=400, width_field=400)
    org_capa = models.ImageField(upload_to=None)
    org_bio = models.TextField(max_length=240)
    org_projeto = models.ForeignKey("projetos.Projeto",on_delete=models.CASCADE,null=True)
    org_equipe = models.ForeignKey("equipe.Equipe", on_delete=models.CASCADE, null=True)
    """**Entendemos os usr_likes etc, como formas de referenciar a Organizacao na qual o usuario deu like
    pode ser necessario adicionar os org_likes etc, referenciando quais usuarios a org deu like**"""
    def __str__():
        return self.org_nome

from django.db import models
"""from equipe.models import Equipe
from usuario.models import Usuario
from posts.models import Post
from organizacao.models import Organizacao"""

class Projeto(models.Model):
    prj_id = models.AutoField(primary_key=True)
    prj_nome = models.CharField("Nome", max_length=50,null=False, blank=False)
    prj_criador = models.OneToOneField("organizacao.Organizacao",on_delete=models.CASCADE)#Falta on_delete
    prj_data_criado = models.DateTimeField(auto_now=True)
    prj_data_modificado = models.DateTimeField(auto_now_add=True)
    prj_descricao = models.TextField(max_length=600, null = False,blank=False)
    prj_capa = models.ImageField(upload_to=None)
    prj_equipe = models.OneToOneField("equipe.Equipe",on_delete=models.CASCADE)#Falta on_delete
    prj_likes = models.ForeignKey("usuario.Usuario",on_delete=models.CASCADE)#Falta on_delete

    def __str__():
        return self.prj_nome

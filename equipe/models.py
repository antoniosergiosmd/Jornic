from django.db import models
"""from projetos.models import Projeto
from usuario.models import Usuario
from posts.models import Post
from organizacao.models import Organizacao"""

class Equipe(models.Model):
    eqp_id = models.AutoField(primary_key=True)
    eqp_criador = models.OneToOneField("organizacao.Organizacao",on_delete=models.CASCADE)#Falta on_delete
    eqp_lider = models.OneToOneField("usuario.Usuario",on_delete=models.CASCADE)#Falta on_delete
    eqp_projeto = models.OneToOneField("projetos.Projeto",on_delete=models.CASCADE)#Falta on_delete
    eqp_data_criado = models.DateTimeField(auto_now=True)
    eqp_data_modificado = models.DateTimeField(auto_now_add=True)
    eqp_membros = models.ManyToManyField("usuario.Usuario",related_name='membros')#Falta on_delete
    eqp_avaliacao = models.IntegerField()#não conseguimos colocar um min/max
    #eqp_likes = ???

    def __str__():
        return self.eqp_projeto.prj_criador

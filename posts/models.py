from django.db import models
"""from equipe.models import Equipe
from usuario.models import Usuario
from projetos.models import Projeto
from organizacao.models import Organizacao"""

class Post(models.Model):
    pst_id = models.AutoField(primary_key=True)
    pst_criador = models.OneToOneField("usuario.Usuario",on_delete=models.CASCADE)#Falta on_delete
    pst_data_criado = models.DateTimeField(auto_now=True)
    pst_data_modificado = models.DateTimeField(auto_now_add=True)
    pst_conteudo = models.TextField(max_length=1000, null = False,blank=False)
    #pst_likes = ???
    pst_comentarios = models.TextField(max_length=400)#como faria para relacionar com algum usuario??
    #pst_compartilhamentos = ???

    def __str__():
        return self.pst_criador.usr_nome

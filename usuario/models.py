from django.db import models
"""from equipe.models import Equipe
from projetos.models import Projeto
from posts.models import Post
from organizacao.models import Organizacao"""

class Usuario(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_nome = models.CharField("Nome", max_length=50,null=False, blank=False)
    usr_nascimento = models.DateField("Data de Nascimento")
    usr_cidade = models.CharField("Cidade",max_length=50,null=False, blank=False)
    usr_estado = models.CharField("Estado (UF)",max_length=2,null=False, blank=False)
    usr_area = models.CharField("Area de Atuação",max_length=20,null=False, blank=False)
    usr_cargo = models.CharField("Cargo", max_length=30,null=False, blank=False)
    usr_email = models.EmailField(max_length=254)
    usr_telefone = models.IntegerField(null=False, blank=False)
    usr_senha = models.CharField(max_length=100,null=False, blank=False)
    usr_avatar = models.ImageField(upload_to=None, height_field=400, width_field=400)
    usr_capa = models.ImageField(upload_to=None)
    usr_bio = models.TextField(max_length=240)
    usr_projeto = models.ForeignKey("projetos.Projeto",on_delete=models.CASCADE,null=True)
    usr_equipe = models.ForeignKey("equipe.Equipe", on_delete=models.CASCADE, null=True)
    #Entendemos desta forma/Talvez precisa corrigir
    usr_likes = models.ManyToManyField("organizacao.Organizacao", related_name = 'likes')
    usr_matchs = models.ManyToManyField("organizacao.Organizacao")
    usr_plano = models.BooleanField(default=False)
    usr_post = models.ForeignKey("posts.Post",on_delete=models.CASCADE)

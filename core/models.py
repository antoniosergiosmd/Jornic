from django.db import models

"""class Usuario(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_nome = models.CharField("Nome", max_length=50,null=False, blank=False)
    usr_nascimento = models.DateField("Data de Nascimento")
    usr_cidade = models.CharField("Cidade",max_length=50,null=False, blank=False)
    usr_estado = models.CharField("Estado (UF)",max_length=2,null=False, blank=False)
    usr_area = models.CharField("Area de Atuação",max_length=20,null=False, blank=False)
    usr_cargo = models.CharField("Cargo", max_length=30,null=False, blank=False)
    usr_email = models.EmailField(max_length=254)
    usr_telefone = models.IntegerField(max_length=11,null=False, blank=False)
    usr_senha = models.CharField(max_length=100,null=False, blank=False)
    usr_avatar = models.ImageField(upload_to=None, height_field=400, width_field=400)
    usr_capa = models.ImageField(upload_to=None)
    usr_bio = models.TextField(max_length=240)
    usr_projeto = models.ForeignKey(Projeto,on_delete=models.CASCADE,null=True)
    usr_equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    #Entendemos desta forma/Talvez precisa corrigir
    usr_likes = models.ManyTooManyField(Organizacao)
    usr_matchs = models.ManyTooManyField(Organizacao)
    usr_plano = models.BooleanFiedl(default=False)
    usr_post = models.ForeignKey(Post)

    def __str__():
        return self.usr_nome

class Organizacao(models.Model):
    org_id = models.AutoField(primary_key=True)
    org_nome = models.CharField("Nome", max_length=50,null=False, blank=False)
    org_fundacao = models.DateField("Fundação")
    org_cidade = models.CharField("Cidade",max_length=50,null=False, blank=False)
    org_estado = models.CharField("Estado (UF)",max_length=2,null=False, blank=False)
    org_area = models.CharField("Area de Atuação",max_length=20,null=False, blank=False)
    org_email = models.EmailField(max_length=254)
    org_telefone = models.IntegerField(max_length=11,null=False, blank=False)
    org_senha = models.CharField(max_length=100,null=False, blank=False)
    org_avatar = models.ImageField(upload_to=None, height_field=400, width_field=400)
    org_capa = models.ImageField(upload_to=None)
    org_bio = models.TextField(max_length=240)
    org_projeto = models.ForeignKey(Projeto,on_delete=models.CASCADE,null=True)
    org_equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    **Entendemos os usr_likes etc, como formas de referenciar a Organizacao na qual o usuario deu like
    pode ser necessario adicionar os org_likes etc, referenciando quais usuarios a org deu like**
    def __str__():
        return self.org_nome

class Post(models.Model):
    pst_id = models.AutoField(primary_key=True)
    pst_criador = models.OneToOneField(Usuario)#Falta on_delete
    pst_data_criado = models.DateTimeField(auto_now=True)
    pst_data_modificado = models.DateTimeField(auto_now_add=True)
    pst_conteudo = TextField(max_length=1000, null = False,blank=False)
    #pst_likes = ???
    pst_comentarios = TextField(max_length=400)#como faria para relacionar com algum usuario??
    #pst_compartilhamentos = ???

    def __str__():
        return self.pst_criador.usr_nome

class Projeto(models.Model):
    prj_id = models.AutoField(primary_key=True)
    prj_nome = models.CharField("Nome", max_length=50,null=False, blank=False)
    prj_criador = models.OneToOneField(Organizacao)#Falta on_delete
    prj_data_criado = models.DateTimeField(auto_now=True)
    prj_data_modificado = models.DateTimeField(auto_now_add=True)
    prj_descricao = TextField(max_length=600, null = False,blank=False)
    prj_capa = models.ImageField(upload_to=None)
    prj_equipe = models.OneToOneField(Equipe)#Falta on_delete
    prj_likes = models.ForeignKey(Usuario)#Falta on_delete

    def __str__():
        return self.prj_nome

class Equipe(models.Model):
    eqp_id = models.AutoField(primary_key=True)
    eqp_criador = models.OneToOneField(Organizacao)#Falta on_delete
    eqp_lider = models.OneToOneField(Usuario)#Falta on_delete
    eqp_projeto = models.OneToOneField(Projeto)#Falta on_delete
    eqp_data_criado = models.DateTimeField(auto_now=True)
    eqp_data_modificado = models.DateTimeField(auto_now_add=True)
    eqp_membros = models.ManyTooManyField(Usuario)#Falta on_delete
    eqp_avaliacao = models.IntegerField(max_length=1)#não conseguimos colocar um min/max
    #eqp_likes = ???

    def __str__():
        return self.eqp_projeto.prj_criador"""

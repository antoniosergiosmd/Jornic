# Generated by Django 3.0.3 on 2020-09-16 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projetos', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='prj_likes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario'),
        ),
    ]

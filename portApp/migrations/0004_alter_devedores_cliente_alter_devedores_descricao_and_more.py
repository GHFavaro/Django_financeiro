# Generated by Django 4.2.11 on 2024-04-29 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portApp', '0003_alter_devedores_cliente_alter_devedores_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devedores',
            name='cliente',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='devedores',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='devedores',
            name='divida',
            field=models.FloatField(),
        ),
    ]
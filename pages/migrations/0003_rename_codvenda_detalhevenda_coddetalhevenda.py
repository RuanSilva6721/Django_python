# Generated by Django 4.1 on 2022-08-25 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_produto_infproduto"),
    ]

    operations = [
        migrations.RenameField(
            model_name="detalhevenda",
            old_name="codVenda",
            new_name="codDetalheVenda",
        ),
    ]

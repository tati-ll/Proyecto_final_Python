# Generated by Django 4.2.3 on 2023-08-10 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_categoria_alter_post_options_post_categoria"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categoria",
            options={"verbose_name_plural": "categorias"},
        ),
    ]

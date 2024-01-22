# Generated by Django 4.2.6 on 2024-01-21 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_bookinstance_borrower_alter_book_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
    ]
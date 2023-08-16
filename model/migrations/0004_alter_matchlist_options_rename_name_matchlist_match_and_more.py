# Generated by Django 4.2.4 on 2023-08-14 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_alter_matchlist_options_alter_stadium_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matchlist',
            options={'ordering': ['match'], 'verbose_name_plural': 'matchlist'},
        ),
        migrations.RenameField(
            model_name='matchlist',
            old_name='name',
            new_name='match',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='matchname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='model.matchlist'),
        ),
    ]
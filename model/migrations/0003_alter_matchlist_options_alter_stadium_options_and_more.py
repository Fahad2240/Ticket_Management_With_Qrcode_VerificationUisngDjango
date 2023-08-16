# Generated by Django 4.2.4 on 2023-08-14 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_alter_ticket_matchname_alter_ticket_stad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matchlist',
            options={'ordering': ['name'], 'verbose_name_plural': 'Matches'},
        ),
        migrations.AlterModelOptions(
            name='stadium',
            options={'ordering': ['nameofstadium'], 'verbose_name_plural': 'Stadium'},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='matchname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='model.matchlist'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='stad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stad', to='model.stadium'),
        ),
    ]

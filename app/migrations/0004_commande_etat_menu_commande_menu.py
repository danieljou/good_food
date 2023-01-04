# Generated by Django 4.1.4 on 2023-01-03 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='etat',
            field=models.CharField(choices=[('En cours', 'En cours'), ('Livrée', 'Livrée'), ('Annulée', 'Annulée')], default='En cours', max_length=50),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_du_menu', models.CharField(max_length=50)),
                ('liste_des_plats', models.ManyToManyField(related_name='repas', to='app.repas')),
            ],
        ),
        migrations.CreateModel(
            name='Commande_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(verbose_name='Quantité')),
                ('date_de_commande', models.DateField(auto_now_add=True)),
                ('date_de_livraison', models.DateField()),
                ('etat', models.CharField(choices=[('En cours', 'En cours'), ('Livrée', 'Livrée'), ('Annulée', 'Annulée')], default='En cours', max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.menu')),
            ],
        ),
    ]

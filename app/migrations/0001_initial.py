# Generated by Django 3.1.4 on 2021-01-27 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('utilsateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('addresse', models.CharField(help_text='Numero, Rue', max_length=200, null=True)),
                ('identifiantCin_Nif', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('dossier', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.diagnostic')),
                ('ordonnance', models.CharField(max_length=500)),
                ('notesImportantes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('dossier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.dossier')),
            ],
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='dossier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.dossier'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-02 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombCarrera', models.CharField(max_length=50)),
                ('numCLiclos', models.IntegerField(default=5)),
                ('numCreditos', models.IntegerField(default=120)),
                ('codCarrera', models.CharField(max_length=10)),
                ('numdocentes', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Paralelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.IntegerField(default=5)),
                ('nombre', models.CharField(max_length=50)),
                ('numeroEstudiantes', models.CharField(max_length=50)),
                ('Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holamundo.carrera')),
            ],
        ),
    ]

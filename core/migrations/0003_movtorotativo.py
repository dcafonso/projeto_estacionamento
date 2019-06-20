# Generated by Django 2.2.2 on 2019-06-20 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_parametro'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovtoRotativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField()),
                ('saida', models.DateTimeField(blank=True)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pago', models.BooleanField(default=False)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo')),
            ],
        ),
    ]

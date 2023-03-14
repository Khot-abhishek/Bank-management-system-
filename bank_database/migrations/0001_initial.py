# Generated by Django 4.1.7 on 2023-03-14 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('m_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=120)),
                ('gender', models.CharField(max_length=7)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=10)),
                ('account_number', models.IntegerField()),
                ('balance', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='bank_database.user')),
            ],
        ),
    ]

# Generated by Django 5.0.7 on 2024-09-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="is_superadmin",
            new_name="is_superuser",
        ),
        migrations.AlterField(
            model_name="account",
            name="date_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="date_joined",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="last_login",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="account",
            name="phone_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

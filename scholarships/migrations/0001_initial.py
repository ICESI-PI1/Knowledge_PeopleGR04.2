
# Generated by Django 4.2.1 on 2023-06-04 05:08


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),

    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stratum', models.CharField(max_length=2)),
                ('photocopy_id', models.FileField(upload_to='files/')),
                ('motivational_letter', models.TextField(max_length=2000)),
                ('certificate', models.FileField(upload_to='files/')),
                ('value_period', models.IntegerField()),
                ('icfes_score', models.IntegerField()),
                ('period_current', models.IntegerField()),
                ('program_adm', models.CharField(max_length=40)),
                ('application_type', models.CharField(choices=[('NI', 'Nuevo Ingreso'), ('A', 'Antiguo')], max_length=40)),
                ('state', models.CharField(choices=[('P', 'Pendiente'), ('A', 'Aceptada'), ('R', 'Rechazada')], max_length=30)),
                ('total_periods', models.IntegerField()),
                ('active', models.CharField(choices=[('AC', 'Activo'), ('IN', 'Inactivo')], default='Activo', max_length=20)),
                ('date_application', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_transaction', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('payment', models.CharField(max_length=120)),
                ('type_pay', models.CharField(choices=[('PSE', 'PSE'), ('Cards', 'Card'), ('PayPal', 'PayPal')], max_length=200)),

                ('donor_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donator', to=settings.AUTH_USER_MODEL)),
                ('institution_donation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='users.institution')),
                ('scolarship_donation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='scholarships.scholarship')),
            ],
        ),
        migrations.CreateModel(
            name='PartialTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_transaction', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('payment', models.CharField(max_length=120)),
                ('type_pay', models.CharField(choices=[('PSE', 'PSE'), ('Cards', 'Card'), ('PayPal', 'PayPal')], max_length=200, null=True)),
                ('donor_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partialtransaction_donator', to=settings.AUTH_USER_MODEL)),
                ('institution_donation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partialtransaction_donations', to='users.institution')),
                ('scolarship_donation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partialtransaction_donations', to='scholarships.scholarship')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),

            ],
        ),
    ]

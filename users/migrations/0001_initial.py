# Generated by Django 4.2.1 on 2023-06-04 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=100)),
                ('profilePicture', models.ImageField(blank=True, null=True, upload_to='users')),
                ('idType', models.PositiveSmallIntegerField(choices=[(1, 'Tarjeta de Identidad'), (2, 'Cédula de Ciudadanía'), (3, 'Cédula extranjera'), (4, 'NIT')])),
                ('numID', models.CharField(max_length=10)),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Beneficiario'), (2, 'Donante natural'), (3, 'Donante juridico'), (4, 'Institución'), (5, 'Admin')])),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('contact', models.CharField(max_length=15)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Admin',
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], max_length=15)),
            ],
            options={
                'verbose_name': 'Beneficiary',
                'verbose_name_plural': 'Beneficiaries',
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(max_length=255)),
                ('type_institution', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=70)),
                ('money_donation', models.IntegerField(default=0)),
                ('verificationState', models.CharField(choices=[('A', 'Aprobada'), ('P', 'Pendiente'), ('R', 'Rechazada')], default='P', max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='LegalDonor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(max_length=255)),
                ('organization_type', models.CharField(choices=[('foundation', 'Fundación o Beca'), ('company', 'Empresa o Empleador'), ('alumni_association', 'Asociación de Exalumnos'), ('charity', 'Organización Benéfica o Sin Fines de Lucro'), ('community_organization', 'Organización Comunitaria'), ('mentoring_program', 'Programa de Tutoría o Mentoría'), ('religious_organization', 'Organización Religiosa'), ('government', 'Gobierno u Organismo Público')], max_length=50)),
            ],
            options={
                'verbose_name': 'LegalDonor',
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='NaturalDonor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'NaturalDonor',
            },
            bases=('users.user',),
        ),
    ]

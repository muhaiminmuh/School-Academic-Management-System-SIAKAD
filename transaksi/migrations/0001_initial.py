# Generated by Django 2.0.3 on 2018-04-10 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0010_auto_20180403_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='KelasPerkuliahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.Kelas')),
                ('mata_kuliah', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.MataKuliah')),
                ('pengampu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.Dosen')),
                ('ta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.TahunAkademik')),
            ],
        ),
        migrations.CreateModel(
            name='Krs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas_perkuliahan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transaksi.KelasPerkuliahan')),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.Mahasiswa')),
            ],
        ),
    ]

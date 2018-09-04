from django.contrib import admin
from master.models import *

# Register your models here.

class ProgramStudiAdmin (admin.ModelAdmin) :
	list_display = ['kode_progdi', 'nama_progdi']
	list_filter = ()
	search_fields = ['kode_progdi', 'nama_progdi']
	list_per_page = 10

admin.site.register(ProgramStudi, ProgramStudiAdmin)

class MahasiswaAdmin (admin.ModelAdmin) :
	list_display = ['nim','nama','alamat','jenis_kelamin','jenis_daftar','no_telepon','email','progdi']
	list_filter = ('jenis_kelamin','jenis_daftar','progdi')
	search_fields = ['nim','nama']
	list_per_page = 20

admin.site.register(Mahasiswa, MahasiswaAdmin)

class DosenAdmin(admin.ModelAdmin) :
	list_display = ['nidn', 'nama', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'no_telepon', 'email']
	list_filter = ['jenis_kelamin']
	search_fields = ['nidn', 'nama']
	list_per_page = 20

admin.site.register(Dosen, DosenAdmin)

class MataKuliahAdmin (admin.ModelAdmin) :
	list_display = ['progdi', 'kode_matkul', 'nama_matkul', 'sks', 'kelompok_matkul']
	list_filter = ['progdi', 'kelompok_matkul']
	search_fields = ['kode_matkul', 'nama_matkul', 'sks']
	list_per_page = 20

admin.site.register(MataKuliah, MataKuliahAdmin)

class KelasAdmin (admin.ModelAdmin) :
	list_display = ['nama_kelas']
	search_fields = ['nama_kelas']
	list_per_page = 20

admin.site.register(Kelas, KelasAdmin)

class KurikulumAdmin (admin.ModelAdmin ) :
	list_display = ['kode_kurikulum', 'nama_kurikulum']
	list_filter = ['kode_kurikulum']
	search_fields = ['nama_kurikulum']
	list_per_page = 20

admin.site.register(Kurikulum, KurikulumAdmin)

class MataKuliahKurikulumAdmin (admin.ModelAdmin) :
	list_display = ['id', 'kurikulum', 'mata_kuliah']
	list_filter = ['id']
	search_fields = ['kurikulum', 'mata_kuliah']
	list_per_page = 20

admin.site.register(MataKuliahKurikulum, MataKuliahKurikulumAdmin)

class TahunAkademikAdmin(admin.ModelAdmin) :
	list_display = ['id_tahun_akademik', 'tahun', 'semester']
	search_fields = ['id_tahun_akademik', 'tahun', 'semester']
	list_per_page = 20

admin.site.register(TahunAkademik, TahunAkademikAdmin)

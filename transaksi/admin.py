from django.contrib import admin
from transaksi.models import *

# Register your models here.

class KelasPerkuliahanAdmin (admin.ModelAdmin):
	list_display = ['kelas','ta','mata_kuliah', 'pengampu']
	list_filter = ['kelas','ta','mata_kuliah', 'pengampu']
	search_field = []
	list_per_page = 20

admin.site.register(KelasPerkuliahan, KelasPerkuliahanAdmin)

class KrsAdmin (admin.ModelAdmin):
	list_display = ['mahasiswa','kelas_perkuliahan']
	list_filter = ['mahasiswa','kelas_perkuliahan'] # karena semua foreigkey jadi dipanggil semua, semua datanya sudah pasti, krena dipanggil dari tabel lain
	search_field = [] # untuk pencarian
	list_per_page = 20

admin.site.register(Krs, KrsAdmin)

class NilaiAdmin (admin.ModelAdmin):
	list_display = ['krs', 'angka', 'huruf', 'tgl_input']
	list_filter = ['krs']
	search_field = []
	list_per_page = 20

admin.site.register(Nilai, NilaiAdmin)
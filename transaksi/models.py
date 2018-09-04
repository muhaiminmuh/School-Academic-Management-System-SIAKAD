from django.db import models
from master.models import * # memanggil semua model dalam master, sehingga bisa dibuat transaksi

class KelasPerkuliahan(models.Model): # membua class baru didalamnya memanggil dari tabel KELAS, TAHUNAKADEMIK, DLL DALAM FOLDER MASTER
	kelas = models.ForeignKey(Kelas, on_delete = models.PROTECT) # PROTECT digunakan agar ketika data dihapus field" yang terhubung tidak terhapus semua
	ta = models.ForeignKey(TahunAkademik, on_delete = models.PROTECT)
	mata_kuliah = models.ForeignKey(MataKuliah, on_delete = models.PROTECT)
	pengampu = models.ForeignKey(Dosen, on_delete = models.PROTECT)

	def __str__(self):
		return self.kelas.nama_kelas + " - " + self.ta.tahun + " " + self.ta.semester + " - " + self.mata_kuliah.nama_matkul

class Krs(models.Model):
	mahasiswa = models.ForeignKey(Mahasiswa, on_delete = models.PROTECT)
	kelas_perkuliahan = models.ForeignKey(KelasPerkuliahan, on_delete = models.PROTECT)

	def __str__(self):
		return self.mahasiswa.nim + " " + self.mahasiswa.nama + " - " + self.kelas_perkuliahan.kelas.nama_kelas + " - " + self.kelas_perkuliahan.mata_kuliah.nama_matkul

class Nilai(models.Model):

	nilai_huruf = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D'),
		('E', 'E'),
	)
	krs = models.ForeignKey(Krs, on_delete = models.PROTECT)
	angka = models.DecimalField(max_digits=5, decimal_places=2 ,blank=True)
	huruf = models.CharField(max_length=1, choices=nilai_huruf)
	tgl_input = models.DateField()

	def __char__(self):
		return self.krs.mahasiswa + " " + self.krs.kelas_perkuliahan + " " + self.angka
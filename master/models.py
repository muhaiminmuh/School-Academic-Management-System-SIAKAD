from django.db import models

# Create your models here.

class ProgramStudi (models.Model) :
	kode_progdi = models.CharField(max_length=2, primary_key=True)
	nama_progdi = models.CharField(max_length=100)

	def __str__(self) :
		return self.nama_progdi

class Mahasiswa (models.Model) :
	JK = (
			('L', 'Laki-laki'),
			('P', 'Perempuan'),

	)
	jenis_daftar = (
			('Regular', 'Regular'),
			('Transfer', 'Transfer')
	)

	nim = models.CharField(max_length=9, primary_key=True)
	nama = models.CharField(max_length=150)
	alamat = models.TextField()
	jenis_kelamin = models.CharField(max_length=1, choices=JK)
	jenis_daftar = models.CharField(max_length=10, choices=jenis_daftar)
	no_telepon = models.CharField(max_length=30, blank=True)
	email = models.CharField(max_length=100, blank=True)
	progdi = models.ForeignKey(ProgramStudi, on_delete=models.PROTECT)

	def __str__(self) :
		return self.nama

class Dosen (models.Model) :
	JK = (
			('L', 'Laki-laki'),
			('P', 'Perempuan'),
	)

	nidn = models.CharField(max_length=12, primary_key=True)
	nama = models.CharField(max_length=150)
	tempat_lahir = models.CharField(max_length=100)
	tanggal_lahir = models.DateField()
	alamat = models.TextField()
	jenis_kelamin = models.CharField(max_length=1, choices=JK)
	no_telepon = models.CharField(max_length=30, blank=True)
	email = models.CharField(max_length=100, blank=True)

	def __str__(self) :
		return self.nidn + " - " + self.nama

class MataKuliah (models.Model) :
	kelompok_matkul = (
		("A", "MPK-Pengembangan Kepribadian"),
		("B", "MKK-Keilmuan dan Ketrampilan"),
		("C", "MKB-Keahlian Berkarya"),
		("D", "MPB-Perilaku Berkarya"),
		("E", "MBB-Berkehidupan Bermasyarakat"),
		("F", "MKU/MKDU"),
		("G", "MKDK"),
		("H", "MKK")
	)

	progdi = models.ForeignKey(ProgramStudi, on_delete=models.PROTECT)
	kode_matkul = models.CharField(max_length=10, primary_key=True)
	nama_matkul = models.CharField(max_length=150)
	sks = models.IntegerField()
	kelompok_matkul = models.CharField(max_length=10, choices=kelompok_matkul)

	def __str__(self) :
		return self.kode_matkul + " - " + self.nama_matkul

class Kelas (models.Model) :
	nama_kelas = models.CharField(max_length=10, primary_key=True)

	def __str__(self) :
		return self.nama_kelas

class Kurikulum (models.Model) :
	kode_kurikulum = models.CharField(max_length=30, primary_key=True)
	nama_kurikulum = models.CharField(max_length=100)

	def __str__(self) :
		return self.nama_kurikulum

class MataKuliahKurikulum (models.Model) :
	id = models.AutoField(primary_key=True)
	kurikulum = models.ForeignKey(Kurikulum, on_delete=models.PROTECT)
	mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.PROTECT)

	def __str__(self) :
		return str(self.id)

class TahunAkademik (models.Model) :
	semester = (
		("Ganjil", "Ganjil"),
		("Genap", "Genap")
	)

	id_tahun_akademik = models.AutoField(primary_key=True)
	tahun = models.CharField(max_length=11)
	semester = models.CharField(max_length=6, choices=semester)

	def __str__(self) :
		return self.tahun + " - " + self.semester

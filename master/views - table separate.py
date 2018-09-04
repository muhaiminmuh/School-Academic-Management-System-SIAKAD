from django.shortcuts import render
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle 
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle 
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import A4, landscape 
from reportlab.lib import colors 
from django.http import HttpResponse 

#import semua class dari master.models 
from master.models import * 
from transaksi.models import *
 
def cetak_mahasiswa(request):     
	# pengaturan respon berformat pdf     
	namaFile = "Lap_Muhaimin.pdf"     
	response = HttpResponse(content_type='application/pdf')     
	response['Content-Disposition'] = 'attachment; filename="' + namaFile + '"' 

    # mengambil data mahasiswa     
	data = Mahasiswa.objects.all()

    #membuat variabel table_data yang digunakan untuk mengisi tabel     
	table_data = []
	table_data2 = []
 
    #membuat judul/header tabel     
	table_data.append([ "NIM", "Nama", "Alamat","Jenis Kelamin" ])
	table_data2.append(["Jenis Daftar", "Telepon", "Email", "Program Studi" ])

    #mengisi tabel     
    #nama field disesuaikan dengan class Mahasiswa yang ada di dalam master     
	for item in data:         
		table_data.append([ item.nim, item.nama, item.alamat, item.jenis_kelamin])      
 
	for item in data:
 		table_data2.append([ item.jenis_daftar, item.no_telepon, item.email, item.progdi ])
    # membuat dokumen baru     
	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)     
	styles = getSampleStyleSheet()

    # pengaturan tabel di pdf     
	table_style = TableStyle([                                
    							('ALIGN',(1,1),(-2,-2),'RIGHT'),                                
     							('VALIGN',(0,0),(0,-1),'TOP'),                                
     							('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),                                
     							('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ])

    #Membuat Tabel dengan isi table_data     
	mahasiswa_table = Table(table_data)
	mahasiswa_table2 = Table(table_data2)
	mahasiswa_table.setStyle(table_style)
	mahasiswa_table2.setStyle(table_style)

    # mengisi konten pdf     
	konten = []     
	konten.append(Paragraph('LAPORAN MAHASISWA', styles['Title']))     
	konten.append(Spacer(1,12))     
	konten.append(mahasiswa_table)
	konten.append(mahasiswa_table2)
    # menghasilkan/generate pdf untuk diunduh     
	doc.build(konten) 

	return response

def grafik_mahasiswa(request) :

	#ambil data mahasiswa
	dataMahasiswa = Mahasiswa.objects.all();

	#membuat data grafik
	data_grafik = []


	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'L'
	jmlLaki2 = dataMahasiswa.filter(jenis_kelamin='L'). count()
	data_grafik.append({"name" : "Laki-laki", "y":jmlLaki2})

	#ambil jumlah mahasiswa dengan filter jenis kelamin = 'P'
	jmlPerempuan = dataMahasiswa.filter(jenis_kelamin='P'). count()
	data_grafik.append({"name" : "Perempuan", "y":jmlPerempuan})

	#tampilkan data_grafik dalam format json
	json_grafik = json.dumps(data_grafik)

	#tampilkan file template grafik_mahasiswa.html dengan membawa nilai json_grafik
	return render(request,'grafik_mahasiswa.html',{'json_grafik':json_grafik}) 
 
 

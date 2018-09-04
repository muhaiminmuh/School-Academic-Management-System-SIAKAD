# School Academic Management System SIAKAD

Merupakan website akademik siakad sederhana yang dibangun dengan framework django


# Requirement
* python 3
* pip
* virtualenvwrapper-win
* django
* mysqlclient
* reportlab


# Installation (windows)
1. Intall python 3
2. Install pip
3. Open Command Prompt, and type  
	* pip  install virtualenvwrapper-win
	* mkvirtualenv academic
	* workon akademic
	* pip  install  mysqlclient
7. Extract & Copy folder ("School-Academic-Management-System-SIAKAD-master") to C:/Users/(userpc)/
8. Open Command Prompt, and type 
	* cd School-Academic-Management-System-SIAKAD-master
	* python manage.py migrate
	* python manage.py createsuperuser
	* python manage.py runserver

Back-End = http://localhost:8000/admin (Login with username & password)
Front-End = http://localhost:8000/
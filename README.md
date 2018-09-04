# School Academic Management System SIAKAD

Merupakan website akademik siakad sederhana yang dibangun dengan framework django


# Requirement
. python 3
. pip
. virtualenvwrapper-win
. django
. mysqlclient
. reportlab

# Installation (windows)
1. Intall python 3
2. Install pip
3. Open cmd -> pip  install virtualenvwrapper-win
4. Open cmd -> mkvirtualenv academic
5. Open cmd -> workon akademic
6. Open cmd -> pip  install  mysqlclient
7. copy folder folder ("School-Academic-Management-System-SIAKAD-master") to C:/Users/(userpc)/
8. Open cmd -> cd School-Academic-Management-System-SIAKAD-master
9. Open cmd -> python manage.py migrate
10. Open cmd -> python   manage.py   createsuperuser (create username & password)
11. python manage.py runserver

Back-End = http://localhost:8000/admin (Login with username & password)
Front-End = http://localhost:8000/



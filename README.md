# URL Shortener
# Description
An application that allows users to shorten long URLs and track the number of times these shortened URLs have been visited.
# Built With:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
# Getting Started
```
https://github.com/CllaudiaB/short_URL.git
```
#### Sur Linux
```
sudo apt-get update
sudo apt-get install python3
```
#### Sur macOS
```
brew install python@3
```
Create a virtual environment in Python using
```
python3 -m venv env
```
To activate your environment, you use the command
```
. env/bin/activate
```
To deactivate the environment, you use the command
```
deactivate
```
You need to navigate to the directory where the requirements.txt file is located in order to install the project's dependencies using the command
```
pip install -r requirements.txt
if python > 3.9 remove backports.zoneinfo in the requirements.txt
```
You need to perform the migrations for the database
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Start the server
```
python3 manage.py runserver
```
# Authors
* Claudia Bura

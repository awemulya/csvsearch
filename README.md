# csvsearch
#assignment work

takes input from form and searches input in csv file

#installing pip

sudo yum install python-pip #fedora

sudo apt-get install python-pip #ubuntu

#virtualenvironment

pip install virtualenv

#creating new environment from virtualenvironment

virtualenv csvenv

#this creates new environment name csvenv

#activate the environment

source csvenv/bin/activate

#install requirements from requirements.txt

  pip install -r requirements.txt

# pull repository
#go to project directory

  cd csvsearch/

# run project

python manage.py migrate

python manage.py runserver

#browse
 http://localhost:8000/home/

 ENJOY



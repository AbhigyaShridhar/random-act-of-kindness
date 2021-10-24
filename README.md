# random-act-of-kindness

## Dependencies
All the dependencies can be checked in the "requirements.txt" file. This project uses python3. 
To install all dependencies perform either "pip3 install -r requirements.txt" or "python3 -m pip install -r requirements.txt"

## django-crispy-forms
Crispy forms are JINJA tags to automatically provide styling to the forms created and rendered by django.

## django-summernote
summernote is a rich text editor which allows font styling, links, videos, and image insertion all using it's pre-defined url patterns.
It is added as an app in the "iiitu/settings.py" file.

## cockroachdb
The website used cockroach db for the database, the certificate can be found in 'certs' directory, and the database settings in the 'YourRandomActOfKindness/settings.py'

## Algorithm for funds distributrion
implementaion of queue in - 'backend/queue.py' and 'backend/models.py'

multilevel feedback queue final implementaion built upon models and queue - 'feedback.py'
the file is called feedback as it is called when the admin site authorises a transaction, and the function then gives "feedback" and updates the state.

#Calhacks 2021
## Project Powered by Cockroach DB

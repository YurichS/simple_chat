# simple_chat

## Virtual environment installing and activating
```
~/Chat$ python3 -m venv venv
~/Chat$ source venv/bin/activate
```
## Required packages installing
```
pip install -r requirements.txt
```
## Secret key
**In folder `~Chat/chat/chat/settings.py` enter string with combination of any symbols**
```
SECRET_KEY = #Enter secret key here
```
## Running server and start testing
**Running server with default settings:**
```
~Chat/chat$ python manage.py runserver
```
**If you want to change server's IP or port, use this command:**
```
~Chat/chat$ python manage.py runserver 0.0.0.0:8000
```

# Project Information

## DEMO VIDEO
https://user-images.githubusercontent.com/87607836/127737352-4d6b463d-7531-4c7c-a800-f233b8a4eb5c.mp4

This project is a webapp based off of Django Python.

It is a prototype bookstore that allows for searching a catalog of books, looking at individual books, and put books into a cart.
When testing make sure Cookies ARE enabled, and you have no ad-block, so the session handling for the cart works properly.

All html files used are based off of the bootstrap framework, to allow for a better looking project while focusing more on the backend code.
The database used is SQLite3, and all handling is through Django

The project consists of 3 webapps: Core, Store, and Cart

Core is the core webapp that doesn't have any features, just stores the main configuration for URLs, HTML templates, settings, etc.

Store is the store webapp that has almost all the features from the project, excluding the cart. The store has a model named Book, containing variables for a book (title, image, etc).

Cart is the cart webapp that has its main functionality in its name. It needed to be seperate from the store webapp because it was a completely different type of application. Session handling required more views and had no models.

For testing, the project is populated with a top 300 books on Amazon csv file. To populate, the SQLite command line was used. There were other methods to do this, like migrating the data with a python function, but SQLite command line was fastest.

NO IMAGES HAVE BEEN UPLOADED TO THE PROJECT, IT IS NOT AN ERROR, THAT IS JUST A DEFAULT IMAGE. There is no reason to upload images for 300 books for testing.

# Instructions (How to run the server on your computer!)

Make sure Python 3.9.5 is installed on your computer.

WINDOWS ONLY:
Open Visual Studio Code

Go to File -> Open Folder...

Open the Bookstore-main folder

If prompted to trust authors, click trust authors

Open the terminal using Ctrl + ' and type:

```
venv\Scripts\activate
```
If you get a signature error, type this, then try again: 

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

It should now say (venv) before your directory. venv is just a folder storing the virtual environment!

To run the server, type:
```
py manage.py runserver
```

Give it a second, and it should load the fully functional server! It will tell you the local address to put into your web browser to test it out. It should be: http://127.0.0.1:8000/


To go to the ADMIN DASHBOARD, type the local address and put /admin. For example http://127.0.0.1:8000/admin
There already is a superuser with username "admin" and password "admin".
In the Admin Dashboard, you will be able to manually create, edit, and delete entries in the database for Books.





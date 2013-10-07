Django-Gami
===========

This project is to facilitate / automate common processes in django development.
It is for the moment configured to work only to work with Technigami repositories.

It is currently undergoing heavy development, and is only intended for internal use.
Feel free to use at your own risk.  We would love feedback, and we want to help
improve the adoption of python web frameworks!

Installation
------------

We recommend having this package globally installed rather than in one specific virtualenv
because we eventually will have this setting up virtualenvs for you.

  sudo pip install https://github.com/Technigami/django-gami/archive/master.zip
  

Basic Usage
-----------

Once you have installed django-gami, you will have a binary executable 'gami'
from a terminal, you can run 'gami <cmd> <argument>'

Supported Commands
------------------

Command: gami init <name>
----------------------------
This command assumes you don't have a git repository set up yet.  It takes a directory containing source code you would like to add 
to our remote hosted git, commits the code, initializes a new repository (if you have permsisions, otherwise you have to request)
pushes it to the newly created remote repository.
                 
* Arguments *
Name - if this is left blank, it will initialize a new repository with the name of the current working directory.


Command: gami clone <repository>
--------------------------------
This is a wrapper around git clone that just saves some typing.  You can leave off the 'git' and the repository url
and just say "git clone <name>" or "git clone <name.git>".


Command: gami workon <name>
----------------------
Either initializes a new virtualenv, or enables the virutalenv with that name on your system.


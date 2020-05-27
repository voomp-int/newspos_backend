# posnews_backend
Backend Microservices

## Configuration Setup: 

## Installation of Python: 

Step 1: Download the Python 3 Installer

- Open a browser window and navigate to the Download page for Windows at python.org.
- Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release - Python 3.x.x. (As of this writing, the latest is Python 3.6.5.)
- Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit.

Step 2: Run the Installer
- Once you have chosen and downloaded an installer, simply run it by double-clicking on the downloaded file. A dialog should appear
- Then just click Install Now. That should be all there is to it. A few minutes later you should have a working Python 3 installation on your system.

Linux Based System:
There is a very good chance your Linux distribution has Python installed already, but it probably won’t be the latest version, and it may be Python 2 instead of Python 3.

To find out what version(s) you have, open a terminal window and try the following commands:

python --version
python2 --version
python3 --version

One or more of these commands should respond with a version, as below:
$ python3 --version
Python 3.6.5

If the version shown is Python 2.x.x or a version of Python 3 that is not the latest (3.6.5 as of this writing), then you will want to install the latest version. The procedure for doing this will depend on the Linux distribution you are running.

## Installation of pipenv

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. Windows is a first--class citizen, in our world.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. 
It also generates the ever--important Pipfile.lock, which is used to produce deterministic builds.

Installation:

If you're on MacOS, you can install Pipenv easily with Homebrew:
$ brew install pipenv

If you're on Windows, Use pip to install Pipenv:
$ pip install --user pipenv

## Steps to host a local server:

- pipenv shell
To create a virtual environment

- pipenv install
To install all the dependencies from Pipfile.lock to the virtual environment

Now,
- python3 nltk_config.py
- Cd into the newspos_backend

To finally run the server: (in the local machine)
- python3 manage.py runserver

Now check localhost:8000

NGROK: Tool used to share your local port to external user

Navigate to the folder where ngrok executable file is located:

- ./ngrok http 8000

*Change ALLOWED_HOSTS to the newly generated url

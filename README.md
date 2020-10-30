<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About The Project](#about-the-project)
  * [Built with](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Usage](#usage)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)
  * [Tools](#tools)

<!-- ABOUT THE PROJECT -->
## About The Project

ProtectUs is a home security system based on the Raspberry Pi platform.
By using facial recognition we are able to recognize a trusted person.
By using bluetooth we are able to disable the system when the user leaves the house.

### Built with

* [OpenCV](https://opencv.org/)
* [Flask](https://flask.palletsprojects.com/)

<!-- GETTING STARTED -->
## Getting Started

We assume you have a Python 3 and corresponding pip package manager installed.
You should have cloned the repository and your current working directory should be the folder to where you cloned the repo to. It is advised to enable a virtual environment before installing packages to isolate them from possible other versions of the same packages.

### Prerequisites

    $ python -m pip install -r requirements.txt

## Usage

To be able to run the Flask application locally you need to set the global variables `FLASK_APP` and `FLASK_ENV`.

Linux

    $ export FLASK_APP=protectus
    $ flask run

Windows

    > set FLASK_APP=protectus
    > flask run

After starting the flask app you can find it under [127.0.0.1:5000](127.0.0.1:5000)

To reinitialize the database

    $ flask init-db

By default the server is only accessible on the system you run the app on. If you trust the users on your network, you can make the server publicly available simply by adding `--host=0.0.0.0` when running the server.

    $ flask run --host=0.0.0.0

To run the WSGI server and enable threading, start the application with Gunicorn. (Make sure the database has been initiliazed)

    $ gunicorn --threads=2 "protectus:create_app()"


## License
[To be determined]

## Authors
* Silas Hoevers
* Pim Langeveld
* Laurens Neinders
* German Savchenko
* Zhongyu Shi

## Acknowledgements
A big thanks has to go out to Adrian Rosebrock and his [pyimagesearch](https://www.pyimagesearch.com/) project. Not only did he provide code that enabled us to easily implement the artificial intelligence features we needed but also wrote articles dedicated to applying it on a Raspberry Pi.

### Tools

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Pycharm (Jetbrains)](https://www.jetbrains.com/pycharm/)


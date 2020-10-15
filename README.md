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

### Built with

* [OpenCV](https://opencv.org/)
* [Flask](https://flask.palletsprojects.com/)

<!-- GETTING STARTED -->
## Getting Started

Follow the instructions below to hook yourself up with a working copy to start development.

### Prerequisites

    $ pip install -r requirements.txt

## Usage

To be able to run the Flask application locally you need to set the global variables `FLASK_APP` and `FLASK_ENV`.

Linux

    $ export FLASK_APP=protectus
    $ export FLASK_ENV=development
    $ flask run

Windows

    > set FLASK_APP=protectus
    > set FLASK_ENV=development
    > flask run

After starting the flask app you can find it under [127.0.0.1:5000](127.0.0.1:5000)

To reinitialize the database

    $ flask init-db

## License
[To be determined]

## Authors
* Silas Hoevers
* Pim Langeveld
* Laurens Neinders
* German Savchenko
* Zhongyu Shi

## Acknowledgements

### Tools

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Pycharm (Jetbrains)](https://www.jetbrains.com/pycharm/)


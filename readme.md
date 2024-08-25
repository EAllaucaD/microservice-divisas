

<!-- ABOUT THE PROJECT -->
## About The Project : FOREIGN_EXCHANGE

This Python project uses Docker and a currency conversion API, providing an automated and scalable solution for performing currency conversions. Docker ensures the portability and consistency of the development environment, while the API allows access to up-to-date exchange rates. This tool is ideal for financial, commercial applications or any environment that requires accurate and timely conversions between different currencies.
Why this program fills a need

This application complies with the basic principle of microservice.

    Efficiency: Automates the currency conversion process, eliminating the need for repetitive manual calculations.
    Accuracy: Uses an updated API to ensure accurate and reliable exchange rates.
    Portability: Encapsulation in Docker ensures that the program runs consistently on various systems and platforms.

This project offers a robust and easy to implement solution for any application requiring automated currency conversion functionalities.





## GROUP :
EDWIN ALLAUCA

SEBASTIÁN CARRERA

### Built With
Python

Flask



## Getting Started and Prerequisites
Prerequisites and Installation

1. Get a free API Key at  https://www.exchangerate-api.com/

        API_KEY= 'API KEY ' in .env (Create it in the root of the project)

2. This is an example of how to list things you need execute.
    pip install -r requirements.txt




<!-- USAGE EXAMPLES -->

## Usage

You can use this project: LOCAL
1. Download the app or the zip from github.
2. To run through the console the application is python divisas.py
3. You can use the port 127.0.0.1:5000


OTHER: DOCKER

1. Have docker installed.
   
2. Download the app

3. Opening a terminal and then the docker file we can execute the command docker build -t divisas .

4. To run the application
       docker run -it --publish 5000:5000 divisas

6. Or run using
       docker -compose up

## Example

Once the application has been executed, you can enter the value of money to be converted.

In this case, the currency that has the value is USD and you want to transform it you must enter the EUR.

![Captura de pantalla 2024-07-08 121451](https://github.com/EAllaucaD/foreign_exchange/assets/135485982/24d04343-cd38-4f7c-951e-63751b1f401a)


![Captura de pantalla 2024-07-08 121457](https://github.com/EAllaucaD/foreign_exchange/assets/135485982/1b8aa2bd-e924-426c-a906-4894f1cd5763)


## Cloud Provider in RAILWAY
(You can only access when the service is up by the team.)

https://foreignexchange-production.up.railway.app/



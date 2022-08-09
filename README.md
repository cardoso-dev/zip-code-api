# Postal Code API

## About the project

This project is a single API for consulting mexican zip codes related data.

The API has only one endpoint `/api/zip-codes/{zip_code}` to GET the data related to a specific zip code.

The source data comes from [correos de México website](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx)

The project is developed using the following stack
- [Laravel framework](https://laravel.com/)
- [Mongodb](https://mongodb.com/) as database
- [Docker](https://www.docker.com/) as container system

## Solution

The solution developed followed the describe steps:

- Download source data from correos de Mexico, the site offers three formats: excel, txt and xml. Download xml format.
- Transform the xml file to a json format file, for this use the python script already included in this repository.
- Create a NoSQL database using the json from the previos step.
- Develop a single endpoint API with Laravel consulting the DB created in the previous step.
- To make easy the development process everything is containerized using docker.

For further details read the following section.

## Installation steps

Before installing a copy and in order to be able to complete the process you need to have a system with the following software already installed:

- [git](https://git-scm.com/)
- [python](https://www.python.org/) *version 3.x*
- [pip](https://pypi.org/project/pip/)
- [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/)

To install a development copy environment follow the next steps: 

- Clone the project:
```bash
$ git clone https://github.com/cardoso-dev/zip-code-api
```

- Create the `.env` file, you can copy the .env.example, be sure to add the following lines:

```
MONGO_DB_HOST=postalcode_mongodb
MONGO_DB_PORT=27017
MONGO_DB_DATABASE=postcodes
```

- Download xml source data [from here](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx). Uncompress the xml file and put it whitin the project folder `/postalcode_docker/CPdescarga.xml`. (**Important to keep the same name as described: CPdescarga.xml**)

- Use the script `convert_xml_to_json.py` in `/postalcode_docker/` to transform the xml file to a json file:
```bash
$ cd postalcode_docker/
$ pip3 install xmltodict # you can use a virtualenv if you prefer so
$ python3 convert_xml_to_json.py
```

- With the json generated we are ready to build the docker images and start the containers, read carefully and run the following commands doing wth the comments say:
```bash
$ cd postalcode_docker/ # change path if you are in the root of the project
# edit the docker-compose.yml file, line 15 with the following
# command: composer install # php artisan serve --host 0.0.0.0
$ docker-compose up # run to build the base images and start containers for the first time
# when finished stop it using ctrl+c
# edit the docker-compose.yml file, to restore line 15
# command: php artisan serve --host 0.0.0.0
$ docker-compose start # run to start the fully working containers
```

This will download the followign docker images: php and mongo, and using the Dockerfile and DockerfileDB will build the base images for the project and start the containers for the first time. Also this will create and seed the database using the json file genearted in the previous step.

At this point you can consume the api endpoint `/api/zip-codes/{zip_code}` replacing the parameter with any valida mexican zip code

- Once the containers are created and running, we can simply stop and start them (there is not need to rebuild unless the base images have new changes)
FROM php

RUN apt-get update && apt-get install -y git

# Install mongo extension
RUN pecl install mongodb \
  && echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/ext-mongodb.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
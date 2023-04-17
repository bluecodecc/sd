FROM php:fpm-alpine
COPY php/opcache.ini /usr/local/etc/php/conf.d/opcache.ini
COPY ./data/ /var/www/html/
RUN docker-php-ext-install opcache &&  docker-php-ext-install pdo_mysql && docker-php-ext-enable pdo_mysql && chmod 777 /var/www/html/usr/uploads
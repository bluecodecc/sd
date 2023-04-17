FROM nginx:alpine
COPY nginx/default.conf /etc/nginx/conf.d
COPY ./data/ /var/www/html/
RUN chmod 777 /var/www/html/usr/uploads
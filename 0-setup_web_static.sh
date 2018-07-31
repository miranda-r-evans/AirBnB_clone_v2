#!/usr/bin/env bash
# configures nginx to serve from /web_static folder
apt-get -y update
apt-get install -y nginx
mkdir /data
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo "hello world" > /data/web_static/releases/test/index.html
rm /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
echo "server {
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;

        root /usr/share/nginx/html;
        index index.html index.htm;

        server_name localhost;

        location / {
                try_files $uri $uri/ =404;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
        }

        location /redirect_me {
                rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }

        error_page 404 /custom_404.html;
        location /custom_404.html {
                root /usr/share/nginx/html;
                internal;
        }
}" | sudo tee /etc/nginx/sites-enabled/default
service nginx restart

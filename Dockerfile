# nginx-gunicorn-flask

FROM debian:11
MAINTAINER Mingzhe Hu <dmriti@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y python3-virtualenv 
RUN apt-get install -y nginx 
RUN apt-get install -y gunicorn 
RUN apt-get install -y supervisor

# Setup flask application
RUN pip install -r requirements.txt

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# Start processes
CMD ["/usr/bin/supervisord"]
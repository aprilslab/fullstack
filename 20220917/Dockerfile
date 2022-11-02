FROM httpd:2.4

ADD httpd.conf /usr/local/apache2/conf/
COPY hello.py /usr/local/apache2/cgi-bin/
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install python3 -q -y
RUN chmod +x /usr/local/apache2/cgi-bin/hello.py
RUN sed -i "s/\r//g" /usr/local/apache2/cgi-bin/hello.py
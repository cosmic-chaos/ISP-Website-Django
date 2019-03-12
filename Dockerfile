# Use an official Python runtime as a parent image
FROM centos:centos7

# Set the working directory to /app
WORKDIR /var/www/html

RUN yum -y update; yum clean all
RUN yum -y install epel-release
RUN yum -y install python-pip git sqlite; yum clean all
RUN pip install --upgrade pip
RUN pip install Django==v1.11
RUN pip install --upgrade django
RUN pip install django-widget-tweaks

# Copy the current directory contents into the container at /app
ADD ISP_Django/html /var/www/html

#ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:80" ] 

EXPOSE 80
FROM django:1.9

RUN pip install --upgrade pip
RUN apt-get update -y && apt-get install -y \
	libjpeg-dev
RUN pip install\
	pillow\
	django-markdown\
	django-bootstrap-form\
	django-google-maps

ADD . /app
WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]

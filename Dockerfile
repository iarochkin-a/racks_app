FROM python:3.12

RUN mkdir DCIM_app

ADD requirements.txt /DCIM_app

WORKDIR /DCIM_app

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm requirements.txt

ADD . /DCIM_app

CMD ["/bin/bash", "start.sh"]

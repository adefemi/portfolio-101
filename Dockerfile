FROM python:3.9

RUN mkdir /portfolio_101

WORKDIR /portfolio_101

COPY . /portfolio_101/

RUN pip install -r requirements.txt

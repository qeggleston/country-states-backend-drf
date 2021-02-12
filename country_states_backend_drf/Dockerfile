FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

COPY ./docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh
CMD ["/docker-entrypoint.sh"]
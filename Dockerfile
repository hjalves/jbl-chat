FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/
RUN python jbl_chat/manage.py collectstatic --noinput
WORKDIR /code/jbl_chat
CMD ["gunicorn", "jbl_chat.wsgi:application", "--bind", "0.0.0.0:8002"]

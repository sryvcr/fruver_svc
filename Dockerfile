FROM python:3.8-alpine AS base

FROM base AS deploy
WORKDIR /usr/app/
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "python", "src/manage.py", "runserver", "0.0.0.0:8000"]

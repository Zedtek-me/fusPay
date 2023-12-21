FROM python:3 AS staging
RUN apt-get update --fix-broken && apt-get -y install
COPY . /project_dir
COPY requirements.txt /project_dir/requirements.txt
RUN pip install requirements.txt
CMD [ "python", "-m", "manage", "runserver", "9000" ]


# production image directives copied from staging
FROM staging AS production
CMD [ "python", "-m", "manage", "runserver", "8000" ]
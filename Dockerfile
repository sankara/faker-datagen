FROM python:3

LABEL MAINTAINER "Sankara Rameswaran"
LABEL REPOSITORY "sankara/faker-datagen"
LABEL GITHUB "sankara/faker-datagen"


WORKDIR /usr/src/app

COPY . ./

RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["python", "./generator.py"]

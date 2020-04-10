FROM python:3

WORKDIR /usr/src/app

COPY . ./

RUN pip instaall --no-cache-dir -r ./requirements.txt

CMD ["python", "./generator.py"]

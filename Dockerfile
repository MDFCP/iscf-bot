FROM python:3

WORKDIR /err

RUN runas err pip install --no-cache-dir -r errbot errbot[slack]

COPY . .

CMD [ "errbot" ]
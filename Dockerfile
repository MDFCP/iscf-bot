FROM python:3

WORKDIR /err

RUN pip install --no-cache-dir -r errbot errbot[slack]

COPY . .

CMD [ "errbot" ]
FROM python:3

WORKDIR /err

RUN pip install --no-cache-dir errbot 
RUN pip install --no-cache-dir errbot[slack]

CMD [ "errbot" ]
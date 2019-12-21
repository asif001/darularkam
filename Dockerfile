FROM python:3.7.5 AS build-env
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY waitForMySQL.sh /usr/local/bin/
RUN apt-get update && \
    apt-get install dos2unix && \
	apt-get -y install default-mysql-client && \
    apt-get clean && \
	dos2unix /usr/local/bin/waitForMySQL.sh && \
	chmod +x /usr/local/bin/waitForMySQL.sh && \
	ln -s /usr/local/bin/waitForMySQL.sh
RUN pip install -r requirements.txt
COPY . /code/
ENTRYPOINT ["waitForMySQL.sh"]
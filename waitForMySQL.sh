#!/bin/bash

set -e
set -x

host="db"
MYSQL_USER="asif"
MYSQL_PASSWORD="4532"
MYSQL_DATABASE="darulakram"
cmd="$@"

until mysql -h"$host" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e 'show databases;'; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "Mysql is up - executing command"

until python manage.py makemigrations; do
  sleep 1
done

until python manage.py migrate; do
  sleep 1
done

>&2 echo "Migration completed ..."

exec $cmd
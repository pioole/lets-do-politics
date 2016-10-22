**********************
postgres db deployment
**********************

Docker setup (first run)
========================

1. Create '.env' file::

    take a look at the '.env-template' file. :)

2. docker-compose up

3. Migrate database

    # in 'lets-do-politics/huffington' directory:
    $ eval $(cat ../.env | sed 's/^/export /')
    $ ./manage_db.py migrate



Docker setup (subsequent runs)
==============================

1.

    docker-compose up -d


DB migration (after any model change)
=====================================

    $ ./manage_db.py makemigrations src
    $ ./manage_db.py migrate

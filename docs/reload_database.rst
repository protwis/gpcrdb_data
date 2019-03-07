Reload database from dump
=========================

* Go to the project root directory on your virtual machine::

    cd /protwis/sites/protwis

* Delete the current database (password: protwis)::

    psql -U protwis -h localhost -d protwis -c 'drop schema public cascade; create schema public;'

* [Optional] Download the newest dump from gpcrdb::

    curl http://files.gpcrdb.org/sql_dump.sql.gz > ~/sql_dump.sql.gz
    gunzip ~/sql_dump.sql.gz

* Load the dump (Either from default location or a location of your choosing)::

    psql -U protwis -h localhost -o protwis < ~/sql_dump.sql;

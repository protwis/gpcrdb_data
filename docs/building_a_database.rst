Building a local database from source data
==========================================

* If you have not completed the :doc:`local installation <local_installation>` of GPCRdb, please do so before continuing.

* Open up a terminal and clone the gpcrdb_data repository from GitHub::

    cd ~/protwis_vagrant
    git clone https://github.com/protwis/gpcrdb_data.git shared/data/protwis/gpcr

* Log into the vagrant VM::

    vagrant ssh
    cd /protwis/sites/protwis

* Clean the current database schema (password: protwis)::

    psql -U protwis -h localhost -d protwis -c 'drop schema public cascade; create schema public;'

* Run migrations::

    /env/bin/python3 manage.py migrate

* Start the build process::

    /env/bin/python3 manage.py build_all -p 4 -t

This will build a test version of the database using only the proteins for which a structure has been determined.
For a full build, remove the -t flag from the build_all command (NOTE: a full build takes a long time, and should not
be run on the development virtual machine)

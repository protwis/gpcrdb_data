Reload database from dump
=========================

* Go to the project root directory on your virtual machine::

    cd /protwis/sites/protwis

* Download the newest dump from gpcrdb [Optional when you already have a dump]::

    curl https://files.gpcrdb.org/protwis_sp.sql.gz > ~/protwis.sql.gz

* Delete the current database (password: protwis)::

    dropdb -U protwis -h localhost protwis

* Load the dump (Either from default location or a location of your choosing)::

    gunzip -c ~/protwis.sql.gz | psql -U protwis -h localhost -d protwis

* Optional steps: 
	* Restart apache2 to fix adminer behavior in some cases::

   		sudo service apache2 restart
 
	* Pull the latest source code from the default branch of `protwis`_ (assuming it is set as the default repository)::

		git stash; git pull; git stash pop

	* Update the static file repository (not for Vagrant setup)::

		<python> manage.py collectstatic

	* Rebuild the local BLAST database::

		<python> manage.py build_blast_database
	
	* Clear the Django caches::

		<python> manage.py clear_cache

.. _protwis: https://github.com/protwis/protwis
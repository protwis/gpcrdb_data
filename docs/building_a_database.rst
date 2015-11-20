Building a local database from source data
==========================================

* If you have not completed the :doc:`local installation <local_installation>` of GPCRdb, please do so before continuing.

* Open up a terminal and clone the gpcrdb_data repository from Bitbucket::
    
    cd ~/protwis_vagrant
    git clone https://bitbucket.org/gpcr/gpcrdb_data.git shared/data/protwis/gpcr

* Log into the vagrant VM::
    
    vagrant ssh

* Start the build process::
    
    cd /vagrant/protwis
    python3 manage.py build_all -p 4 -t

This will build a test version of the database using only the proteins for which a structure has been determined.
For a full build, remove the -t flag from the build_all command (NOTE: a full build takes a long time, and should not
be run on the development virtual machine)
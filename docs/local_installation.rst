Local installation
==================

For development
---------------

This guide describes how to set up a ready-to-go virtual machine with Virtualbox and Vagrant.

Works on Linux, Mac, and Windows.

Prerequisites
^^^^^^^^^^^^^

* `Vagrant`_
* `VirtualBox`_
* `Git`_
* `Bitbucket`_ account

.. _Vagrant: http://www.vagrantup.com
.. _VirtualBox: https://www.virtualbox.org
.. _Git: http://git-scm.com
.. _Bitbucket: http://www.bitbucket.org

Install Vagrant, VirtualBox, and Git, and create a Bitbucket account (if you don't already have one).

Make sure you have the latest version of all three. On Ubuntu, the package manager installs an old version of Vagrant,
so you will have to download and install the latest version from the Vagrant website.

Linux and Mac
^^^^^^^^^^^^^

* Open up a terminal and clone the protwis_vagrant repository from Bitbucket::
    
    git clone https://bitbucket.org/gpcr/protwis_vagrant.git ~/protwis_vagrant
    cd ~/protwis_vagrant

* Install ubuntu/trusty64 Vagrant box::

    vagrant box add ubuntu/trusty64

* Fork the protwis repository by going to https://bitbucket.org/gpcr/protwis and clicking "Fork" in the left menu

* Clone the forked repository into the "shared" directory (replace your-username with your Bitbucket username)::

    cd ~/protwis_vagrant
    git clone https://bitbucket.org/your-username/protwis.git shared/protwis

* Start the vagrant box (this may take a few minutes)::
    
    cd ~/protwis_vagrant
    vagrant up

* Log into the vagrant VM::
    
    vagrant ssh

* Start the built in Django development webserver::
    
    cd /vagrant/protwis
    python3 manage.py runserver 0.0.0.0:8000

You're all set up. The webserver will now be accessible from http://localhost:8000

Windows
^^^^^^^

* Open up Powershell and clone the protwis_vagrant repository from Bitbucket::

    git clone https://bitbucket.org/gpcr/protwis_vagrant.git .\protwis_vagrant
    cd .\protwis_vagrant

* Install ubuntu/trusty64 Vagrant box:

    vagrant box add ubuntu/trusty64

* Fork the protwis repository by going to https://bitbucket.org/gpcr/protwis and clicking "Fork" in the left menu

* Clone the forked repository into the "shared" directory (replace your-username with your Bitbucket username)::

    cd ~/protwis_vagrant
    git clone https://bitbucket.org/your-username/protwis.git .\shared\protwis

* Start the vagrant box (this may take a few minutes)::

    cd ~/protwis_vagrant
    vagrant up

* Log into the vagrant VM using an SSH client, e.g. PuTTY, with the following settings::

    host: 127.0.0.1
    port: 2226
    username: vagrant
    password: vagrant

* Start the built in Django development webserver::
    
    cd /vagrant/protwis
    python3 manage.py runserver 0.0.0.0:8000

You're all set up. The webserver will now be accessible from http://localhost:8000

Other notes
^^^^^^^^^^^

The protwis directory is now shared between the host machine and the virtual machine, and any changes made on the host
machine will be instantly reflected on the server.

To run django commands from the protwis directory, ssh into the VM, and use the "python3" command e.g::
    
    cd ~/protwis_vagrant/
    vagrant ssh
    cd /vagrant/protwis
    python3 manage.py check protein

The database administration tool Adminer is installed and accessible at http://localhost:8001/adminer. Use the
following settings::

    System: PostgreSQL
    Server: localhost
    Username: protwis
    Password: protwis

For internal use
----------------

Coming soon.
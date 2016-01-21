Welcome to GPCRdb's documentation
=================================

GPCRdb contains data, diagrams and web tools for G protein-coupled receptors (GPCRs).
Users can browse all GPCR crystal structures and the largest collections of receptor mutants.
Diagrams can be produced and downloaded to illustrate receptor residues (snake-plot and helix box diagrams) and
relationships (phylogenetic trees). Reference (crystal) structure-based sequence alignments take into account helix
bulges and constrictions, display statistics of amino acid conservation and have been assigned generic
residue numbering for equivalent residues in different receptors

The `source code`_ and `source data`_ are freely available on `GitHub`_.

.. _source code: https://github.com/protwis/protwis
.. _source data: https://github.com/protwis/gpcrdb_data
.. _GitHub: http://github.com

The documentation in organized into four sections:

* :ref:`tutorial`
* :ref:`user-docs`
* :ref:`dev-docs`
* :ref:`about-docs`

.. tutorial:

.. toctree::
    :maxdepth: 2
    :caption: Tutorial

    tutorial_receptors
    tutorial_structures
    tutorial_mutations
    tutorial_sites

.. _user-docs:

.. toctree::
    :maxdepth: 2
    :caption: User documentation

    receptors
    sequences
    structures
    mutations
    sites
    generic_numbering

.. _dev-docs:

.. toctree::
    :maxdepth: 2
    :caption: Developer documentation

    web_services
    contributing
    local_installation
    coding_style
    git_workflow
    reload_database
    building_a_database

.. _about-docs:

.. toctree::
    :maxdepth: 2
    :caption: About GPCRdb

    about
    contact
    citing
    acknowledgements
    legal_notice
    meetings
    linking
    external_servers

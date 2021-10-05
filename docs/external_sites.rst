External GPCR sites
===================

Modeling servers
----------------

`GPCRM`_
~~~~~~~~

GPCRM is a novel method for fast and accurate generation of GPCR models using averaging of multiple template structures
and profile-profile comparison. In particular, GPCRM is the first GPCR structure predictor incorporating two distinct
loop modeling techniques: Modeller and Rosetta together with the filtering of models based on the Z-coordinate.

.. _GPCRM: https://gpcrm.biomodellab.eu/

`scPDB`_
~~~~~~~~

To assist structure-based approaches in drug design, we have processed the PDB to identify binding sites suitable for
the docking of a drug-like ligand and we have so created a database called sc-PDB. The sc-PDB database provides
separated MOL2 files for the ligand, its binding site and the corresponding protein chain(s). Ions and cofactors at the
vicinity of the ligand are included in the protein.

.. _scPDB: http://bioinfo-pharma.u-strasbg.fr/scPDB/

`GPCR-SSFE`_
~~~~~~~~~~~~

The GPCR-Sequence-Structure-Feature-Extractor (SSFE) database provides template suggestions and homology models of the
helical regions of 5025 family A GPCRs. SSFE is based on our published workflow for identifying key sequence and
structural motifs in family A GPCRs which is used to guide template selection and build homology models.

.. _GPCR-SSFE: http://www.ssfa-7tmr.de/ssfe/

`GOMoDo`_
~~~~~~~~~

GOMoDo (GPCR Online Modeling and Docking) is a web server that allows to seamlessly model GPCR structures and dock the 
corresponding ligands to these models in a single consistent pipeline. GOMoDo can automatically perform template choice 
(using HHSearch), homology modeling (with Modeller), binding pocket prediction (with FPocket), and either blind or 
information-driven docking (using AutoDock Vina or HADDOCK, respectively). By combining all these state-of-the-art 
bioinformatic tools, the web server guides the user through the whole procedure, while still permitting manual intervention.

.. _GOMoDo: https://gomodo.grs.kfa-juelich.de

`GPCR-ModSim`_
~~~~~~~~~~~~~~

This server was created to allow any researcher with interest in GPCRs to obtain the most accurate structural and
dynamic information for a given receptor. Here, you can generate a homology-based 3D model of your query GPCR sequence,
and/or further equilibrate your GPCR structure with our all-atom Molecular Dynamics simulation protocol.

.. _GPCR-ModSim: http://gpcr-modsim.org/


`Hybrid MM/CG webserver`_
~~~~~~~~~~~~~~~~~~~~~~~~~

Hybrid Molecular Mechanics/Coarse-Grained (MM/CG) simulations have been shown to help refine ligand poses in human G 
protein-coupled receptors (hGPCRs). The Hybrid MM/CG Webserver takes structures of GPCR/ligand complexes (that can be 
generated with other GPCR-related webservers) and prepares them for running such multiscale simulations. This approach 
allows the description of the ligand, the binding cavity, and the surrounding water molecules at atomistic resolution, 
while coarse-graining the rest of the receptor to reduce the computational cost. The system, prepared and equilibrated 
with the Hybrid MM/CG webserver, can be downloaded and the MM/CG simulation can be continued locally.

.. _MM/CG: https://mmcg.grs.kfa-juelich.de

Others
------

`Guide to Pharmacology`_
~~~~~~~~~~~~~~~~~~~~~~~~

Founded in 1959 as a section of the International Union of Physiological Sciences, the International Union of Basic and
Clinical Pharmacology (IUPHAR) has been independent since 1966. IUPHAR is a member of the International Council for
Science (ICSU) and participates in the work of its scientific committees. It receives international recognition,
particularly by the United Nations Educational, Scientific and Cultural Organization (UNESCO).

.. _Guide to Pharmacology: https://www.guidetopharmacology.org/

`DrGPCR`_
~~~~~~~~~

The Dr. GPCR Ecosystem is a website aiming to connect the general GPCR community through various initiatives such as
Cafe and Connect events to promote networking, product and reagent knowledge sharing, as well as talking science
and business. Similarly, the GPCR Club on LinkedIn and the very first Podcast dedicated to GPCRs are meant to share
information, learn the latest and greatest on GPCR research. Dr. GPCR also seeks to connect GPCR Consultants with clients
and generate cohesion in the international GPCR community at large.

.. _DrGPCR: https://www.drgpcr.com/

`GPCRladies`_
~~~~~~~~~~~~~

GPCRladies is a list of women scientists working in the field of G-protein coupled receptors (GPCRs). It was set up to 
help diversify and balance speakers and participants in GPCR-related conferences, boards and committees.

.. _GPCRladies: https://gpcrladies.com/

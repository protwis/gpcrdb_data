External GPCR servers
===================================

`GPCRM`_
--------

GPCRM is a novel method for fast and accurate generation of GPCR models using averaging of multiple template structures
and profile-profile comparison. In particular, GPCRM is the first GPCR structure predictor incorporating two distinct
loop modeling techniques: Modeller and Rosetta together with the filtering of models based on the Z-coordinate.

.. _GPCRM: http://gpcrm.biomodellab.eu/

`scPDB`_
--------

To assist structure-based approaches in drug design, we have processed the PDB to identify binding sites suitable for
the docking of a drug-like ligand and we have so created a database called sc-PDB. The sc-PDB database provides
separated MOL2 files for the ligand, its binding site and the corresponding protein chain(s). Ions and cofactors at the
vicinity of the ligand are included in the protein.

.. _scPDB: http://cheminfo.u-strasbg.fr/scPDB/

`GPCR-SSFE`_
------------

The GPCR-Sequence-Structure-Feature-Extractor (SSFE) database provides template suggestions and homology models of the
helical regions of 5025 family A GPCRs. SSFE is based on our published workflow for identifying key sequence and
structural motifs in family A GPCRs which is used to guide template selection and build homology models.

.. _GPCR-SSFE: http://www.ssfa-7tmr.de/ssfe/

`GOMoDo`_
---------

This webtool performs automatic homology modeling and ligand docking of GPCR receptors. It uses HHsearch package 1.5.1
for performing sequence alignment. Only GPCR templates are chosen to build 3D model of given sequence by using Modeller
9.10. The obtained 3D model can be verified also with the VADAR server, and then docked with ligands uploaded by users
with both Autodock VINA or HADDOCK. Binding pockets can be predicted by the FPOCKET, and structural alignment of models
needed for VINA docking is performed by LOVOALIGN.

.. _GOMoDo: http://molsim.sci.univr.it/cgi-bin/cona/begin.php

`GPCR-ModSim`_
--------------

This server was created to allow any researcher with interest in GPCRs to obtain the most accurate structural and
dynamic information for a given receptor. Here, you can generate a homology-based 3D model of your query GPCR sequence,
and/or further equilibrate your GPCR structure with our all-atom Molecular Dynamics simulation protocol.

.. _GPCR-ModSim: http://gpcr-modsim.org/
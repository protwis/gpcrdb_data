Structures
=================

Structure browser
-----------------

The structure table shows an annotated list of published GPCR structures. The table can be sorted by each
column by clicking on the header. The search fields below each header can be used to filter the structures, e.g.
show only those with a co-crystallized agonist or X-ray resolution < 2.5 Å.

To view an alignment of the selected structures' sequences, click the "Align" button. Downloading multiple structures
at the same time is available with the "Download" button. The "Show representative" button will filter the table by
only showing structures that are the representative structures for the given receptor in each state. These structures
are the one that have the most GPCRdb generic numbered positions present in the structure and have high resolution.

Structure state
---------------

A 7TM Open IC was determined for all class A structure templates by subtracting the 3x44-7x52 C alpha distance from the 2x41-6x38 
C alpha distance and for all class B structure templates by subtracting the 3x44-7x51 C alpha distance from the 2x41-6x33 C alpha distance. 
These values are now provided in the Structure Browser (`gpcrdb.org/structure`_) 
in the 7TM Open IC (Å) column.

.. _gpcrdb.org/structure: http://gpcrdb.org/structure

==== ==== ==== ==== =====  ========  ============  ======
TM2  TM6  TM3  TM7  Class  Inactive  Intermediate  Active
==== ==== ==== ==== =====  ========  ============  ======
2x41 6x38 3x44 7x52 A      <2        2<=x<=7.15    >7.15
2x41 6x33 3x44 7x51 B      <2.5      2.5<=x<=6     >6
2x41 6x38 3x44 7x52 F      <0        0<=x<=2       >2
==== ==== ==== ==== =====  ========  ============  ======
All Class C structures are, so far, in the inactive state.

This definition is an approach more based on structure than function. The 7TM Open IC resembles a general openness of the intracellular side
of the receptor where coupling of a signaling protein can occur. There are structures where based on ligand properties the structure should
be identified as inactive, however due to a fusion protein on the intracellular side of the receptor, the conformation is more similar to an active
structure (e.g. 5NDD, 5NJ6). Another unusual example is one of the Platelet-activating factor receptor structures (5ZKP), where H8 turns inward the
helical bundle, blocking the chance of signal protein coupling while pushing TM2 outwards.

Structure statistics
--------------------

The statistics page shown a bar graph showing the number of structures available by year (and grouped by the
endogenous ligand type of the receptors), a bar graph showing the resolution ranges of the available structures, and
phylogenetic trees for each receptor class, with receptors with determined structures highlighted.

The graphs are automatically updated when new data is added to GPCRdb, making them ideal for use in publications and
presentations.

Structure superposition
-----------------------

The superposition tool allows users to upload two or more structures (or models) and superpose them based on a
user-specified segment selection. Using the tool is a two step process.

1.  Select structures to upload. Only on reference structure can be uploaded, but multiple structures to superpose on
    the reference can be uploaded. To select many structures for upload, hold down the Control key (or Command on Mac)
    while selecting
2.  After structures have been uploaded, the user is presented with a sequence segment selection page. The user can
    select one or more sequence segments, and/or expand each segment to select the residues within it individually.
    Residues selected individually are grouped into a custom sequence segment.

PDB file residue numbering
--------------------------

The PDB file residue numbering tool adds generic residue numbers from GPCRdb to any GPCR structure or model. This can
be useful when comparing structures visually.

A user simply uploads her structure and downloads a modified version of that structure, where b factors of certain
atoms have been replaced with generic numbers. Note that CA atoms will be assigned a number in GPCRdb notation, and N
atoms will be annotated with Ballesteros-Weinstein scheme.

On the structure download page, users can download scripts to visualize the generic numbers in `PyMOL`_ and `Maestro`_.

.. _PyMOL: http://pymol.org
.. _Maestro: http://www.schrodinger.com/Maestro

Template selection
------------------

Using the template selection tool is a one step process. The user is first presented with a reference receptor
selection page. The selected reference receptor will be compared to the published GPCR structures, making it a useful
tool for selecting templates for homology modeling.

Once a reference receptor has been selected, an annotated table of published GPCR structures, ranked by
similarity to the selected reference receptor is shown. The table can be sorted by each column by clicking on the
header. The search fields below each header can be used to filter the structures, e.g. show only those with a
co-crystallized agonist or X-ray resolution < 2.5 Å.

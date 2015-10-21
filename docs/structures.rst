Structures
=================

Structure browser
-----------------

The structure table shows an annotated list of published GPCR structures. The table can be sorted by each
column by clicking on the header. The search fields below each header can be used to filter the structures, e.g.
show only those with a co-crystallized agonist or X-ray resolution < 2.5 Å.

To view an alignment of the structures' sequences, click the "View alignment" button.

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

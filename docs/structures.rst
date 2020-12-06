Structures
==========

Structure browser
-----------------

The structure table shows an annotated list of published GPCR structures. The table can be sorted by each
column by clicking on the header. The search fields below each header can be used to filter the structures, e.g.
show only those with a co-crystallized agonist or X-ray resolution < 2.5 Å.

To view an alignment of the selected structure sequences, click the "Align" button. Downloading multiple structures
at the same time is available with the "Download" button. The "Show representative" button will filter the table by
only showing structures that are the representative structures for the given receptor in each state. These structures
are the ones which have the most GPCRdb generic numbered positions present in the structure and have high resolution.

Refined structures
------------------

GPCRdb provides regularly updated refined structures where missing segments are modeled using the GPCRdb homology modeling 
pipeline (`Pándy-Szekeres et al. 2018`). This entails modeling missing segments (helix ends, loops, H8), reverting 
mutations to wild type and remodeling distorted regions based on our in-house manual structure curation. The refined 
structures are available on the Structures (`gpcrdb.org/structure`_) and Structure models pages (`gpcrdb.org/structure/homology_models`_).

.. _Pándy-Szekeres et al. 2018: https://doi.org/10.1093/NAR/GKX1109
.. _gpcrdb.org/structure: https://gpcrdb.org/structure
.. _gpcrdb.org/structure/homology_models: https://gpcrdb.org/structure/homology_models

Structure statistics
--------------------

The statistics page shown a bar graph showing the number of structures available by year (and grouped by the
endogenous ligand type of the receptors), a bar graph showing the resolution ranges of the available structures, and
phylogenetic trees for each receptor class, with receptors with determined structures highlighted.

The graphs are automatically updated when new data is added to GPCRdb, making them ideal for use in publications and
presentations.

Structure models
----------------

With every database update GPCRdb builds a homology model repository containing models for every human GPCR in three
different activation states (inactive, intermediate, active). Class T is based on class A and class B2 is based on class B1.
The models are created based on the GPCRdb homology modeling pipeline (`Pándy-Szekeres et al. 2018`_) that utilizes an 
automated chimeric modeling approach. For every model a single main template is selected and atomic coordinates from 
alternative local templates are swapped-in for sections of the model where either the main template is missing coordinates 
or the algorithm predicts a better template based on multiple criteria. These affect helix ends, loops, H8 and structural
anomalies like bulges and constrictions. Furthermore, an in-house rotamer library is applied for side-chains where there
is a mismatch between the modeled receptor and the template. The newest version of the homology models can be found on 
the Structure models page (`gpcrdb.org/structure/homology_models`_) where users can download the older versions as well 
from the Archive.

.. _Pándy-Szekeres et al. 2018: https://doi.org/10.1093/NAR/GKX1109
.. _gpcrdb.org/structure/homology_models: https://gpcrdb.org/structure/homology_models

Structure model statistics
--------------------------

To assess GPCRdb homology models we provide root-mean-square deviation (RMSD) calculations between the first published
experimental structure of a receptor and the latest GPCRdb model before that publishing date. The compared model is in
the same activation state as the experimental structure. After a structure is released, manually annotated structural 
data is added to GPCRdb with the next release. In some cases, there is a delay between the manual annotation and the 
release of the structure; therefore, some model versions can have a later date than the publication date of the modeled 
structure.

For such structural comparisons the method of superpositioning is key. The GPCRdb RMSD calculation workflow employs a
sequence-dependent comparison where atoms that are missing from either the structure or the model are excluded and only 
the 7-transmembrane (7TM) backbone atoms (N, CA, C) determined by GPCRdb sequence alignments are used for the superpositioning.
Sequence-dependent RMSD calculations are carried out from this superpositioned state. For loop segment RMSD scores this 
makes it possible to factor in not only the structural characteristics of the loop but the its position relative to the 
7TM bundle. Futhermore, different properties of the models can be assessed based on which atoms we select for the RMSD
calculations. The actual RMSD calculations were done with the following python code:
round(np.sqrt(sum(sum((array1[1:]-array2[1:])**2))/array1[1:].shape[0]),1)
where array1 and array2 are numpy arrays with atomic coordinates from structure and model respectively. 

The scores currently available for the GPCRdb models:

- Overall all: all atoms
- Overall backbone: all backbone atoms
- 7TM all: all atoms of 7TM residues defined by GPCRdb sequence alignments
- 7TM backbone: backbone atoms of 7TM residues defined by GPCRdb sequence alignments
- H8: Helix 8 backbone atoms
- ICL1: Intracellular loop 1 backbone atoms
- ECL1: Extracellular loop 1 backbone atoms
- ICL2: Intracellular loop 2 backbone atoms
- ECL2: Extracellular loop 2 backbone atoms
- ECL3: Extracellular loop 3 backbone atoms

Parts of these results were published in `Kooistra et al. 2020`_; however some values online differ from values published 
in the paper due to the inclusion of `RosettaGPCR`_ models in the journal calculations. The difference arises from some
missing atoms in those models which leads to a different superpositioning and different atoms included for RMSD calculations.

.. _Kooistra et al. 2020: https://doi.org/10.1093/nar/gkaa1080
.. _RosettaGPCR: http://www.meilerlab.org/index.php/gpcrmodeldb

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

.. _PyMOL: https://pymol.org
.. _Maestro: https://www.schrodinger.com/Maestro

Template selection
------------------

Using the template selection tool is a one step process. The user is first presented with a reference receptor
selection page. The selected reference receptor will be compared to the published GPCR structures, making it a useful
tool for selecting templates for homology modeling.

Once a reference receptor has been selected, an annotated table of published GPCR structures, ranked by
similarity to the selected reference receptor is shown. The table can be sorted by each column by clicking on the
header. The search fields below each header can be used to filter the structures, e.g. show only those with a
co-crystallized agonist or X-ray resolution < 2.5 Å.

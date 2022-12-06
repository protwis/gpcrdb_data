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
pipeline (`Pándy-Szekeres et al. 2018`_). This entails modeling missing segments (helix ends, loops, H8), reverting
mutations to wild type and remodeling distorted regions based on our in-house manual structure curation. The refined
structures are available on the Structures (`gpcrdb.org/structure`_) and Structure models pages (`gpcrdb.org/structure/homology_models`_).

.. _Pándy-Szekeres et al. 2018: https://doi.org/10.1093/NAR/GKX1109
.. _gpcrdb.org/structure: https://gpcrdb.org/structure
.. _gpcrdb.org/structure/homology_models: https://gpcrdb.org/structure/homology_models

Structure statistics
--------------------

The statistics page shows a bar graph with the number of structures available by year (and grouped by the
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

Structure model validation
--------------------------

To assess GPCRdb homology models we provide root-mean-square deviation (RMSD) calculations between the first published
experimental structure of a receptor and the latest GPCRdb model before that publish date. The model is in the same
activation state as the experimental structure. After a structure is released, manually annotated structural data is
added to GPCRdb with the next release. In some cases, there is a delay between the manual annotation and the release
of the structure; therefore, some model versions can have a later date than the publication date of the modeled
structure; however, these do not contain any information from the modeled structure.

For such structural comparisons the superpositioning method is key. The GPCRdb RMSD calculation workflow employs a
sequence-dependent comparison where atoms that are missing from either the structure or the model are excluded and only
the 7-transmembrane (7TM) backbone atoms (N, CA, C) determined by GPCRdb sequence alignments are used for the superpositioning.
All RMSD calculations, which are also sequence-dependent, are carried out from this superpositioned state. For loop segment
RMSD scores, this makes it possible to factor in not only the structural characteristics of the loop but also its position
relative to the 7TM bundle. Furthermore, different properties of the models can be assessed based on which atoms we select for
the RMSD calculations. The RMSD calculations themselves were done with the following python code:

.. highlight:: python
.. code-block:: python

   round(np.sqrt(sum(sum((array1[1:]-array2[1:])**2))/array1[1:].shape[0]),1)

where array1 and array2 are numpy arrays with atomic coordinates from structure and model respectively.

RMSD categories currently available for GPCRdb models:

- Overall all: all atoms
- Overall backbone: all backbone atoms
- 7TM all: all atoms of 7TM residues
- 7TM backbone: backbone atoms of 7TM residues
- H8: Helix 8 backbone atoms
- ICL1: Intracellular loop 1 backbone atoms
- ECL1: Extracellular loop 1 backbone atoms
- ICL2: Intracellular loop 2 backbone atoms
- ECL2: Extracellular loop 2 backbone atoms
- ECL3: Extracellular loop 3 backbone atoms

Structure descriptors
----------------------

* Activation state definition
	The activation state of the structures are defined on the distances between all Cα atoms for residues on the intracellular half of each of the seven transmembrane helices. These distances are also used for the generation of the `Structural similarity trees <structure_comparison.html#structure-similarity-trees>`__ . For each class, structures in complex with a signaling protein are are set as the reference structures for the active state(100% degree activation). Subsequently, structures with a highly closed conformation are set as the reference structures for the inactive state (0% degree activation) based on a maximum distance between 2x46 to 6x37 for all classes except for class F for which the distance between 2x44 to 6x31 is used (maximum distances are 11.9Å, 13Å, 14.5Å, 13Å for classes A, B, C, and F, respectively). The Cα atom distance pairs for each structure are compared to the reference structures and the mean distance to the active structures and the mean distance to the inactive structures are then calculated. If a structure has a low distance to the inactive structures its state is defined as *inactive*, vice versa if a structure has a low distance to the active structures then its state is defined as *active*. However, if both are not the case then the structure is defined as *intermediate*. In some cases, when an unlikely conformation is encountered its state is defined as *other* as is now the case for the structure of the plate-activating factor receptor `5ZKP <https://gpcrdb.org/structure/5ZKP>`__.

	*The degree activation*:  These distances to the reference structure sets are then converted into an "activation score" by substracting the mean distance to the inactive-state structures from the mean distance to the active-state structures. The activation score is converted into a percentage activation based on the minimum and maximum activation scores for all structures in that class.

* TM6 tilt
	The TM6 tilt measure is defined based on the distance between the Ca atoms for the residues 2x46 and 6x37 for all classes except for class F for which the distance between 2x44 and 6x31 is used. For each structure, this distance (when the residues are present) is converted into a percentage by comparing it to the minimum and maximum distance observed in any other structure for that specific class.

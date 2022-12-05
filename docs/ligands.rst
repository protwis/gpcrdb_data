Ligands & Bioactivities
=========

.. _International Union of Basic and Clinical Pharmacology: https://www.guidetopharmacology.org/nomenclature.jsp

Ligand coverage
---------------

The ligand coverage page is designed to showcase the ligand data present in GPCRdb through a fast visualization trees
able to convey the message in a timely fashion. In this page,you will find:

1.  A table at the top, listing the number of unique ligands per receptor class, divided by each class (family).
    Moreover, the table lists also the average number of ligands per GPCR in each class and the total count.
    Lastly, the table lists the number of GPCRs with ligands for each class present in GPCRdb.
2.  Visualization phylogenetic trees for each GPCR class, where each branch points to a different ligand family,
    ending with an inner circle shaded by the amount of ligand data available for that specific GPCR receptor.
    Coloring of that inner circle is in grayscale, whereas light shades of gray may vary between 10 to 500
    ligands, and darker shades of grey up to black add up to more than 1000 compounds targeting that receptor.

Phylogenetic trees be default will show the UniProt name of the different GPCRs, but through a dedicated selection
button users can decide to show the IUPHAR names of those GPCRs. Trees can also be downloaded in several different
formats (SVG, JPG, TIFF and PNG), allowing for high level pictures for publication purposes.

Ligands (ChEMBL, GtP, Ki db)
------------------

The ligand query section provides two different alternatives for investigating the ligands available in GPCRdb:

1.  Querying by receptor
2.  Querying by ligand name, ligand ID, SMILES or Inchikey.


Receptor query
^^^^^^^^^^^^^^

In the receptor based query you will be prompted to select a receptor in the selection table, showing the number
of ligand for each receptor, divided also for drugs that have been approved and those in clinical trials.
After selecting the receptor target, users can choose between two ligand bioactivity browsers.
The ‘Compact (1 row/ligand)’ browser collates all binding or functional bioactivities of a given ligand and source
database on one row by calculating minimum, average and maximum activity across studies.
The ‘Extended (1 row/activity)’ browser instead lists the specific binding affinity or potency value of each study.
The latest GPCRdb release has restructured potency and affinity data into separate tabs. It has also added fold selectivity
values, along with the underlying number of experiments, allowing ligand selection based on their selectivity
for the target of interest relative to all other stored GPCR targets. Both browsers also present information
about vendors from which one can purchase the given ligand along with key physicochemical descriptors

Ligand query
^^^^^^^^^^^^

In the ligand query page you will be able to input either the ligand name, ligand ID (from either database of origin, being
it GPCRdb itself, Guide to Pharmacology, ChEMBL or the PDSP KiDatabase), or structure information (being it SMILES
or Inchikey) in the search textbox comprehensive of autofill. A dropdwon menu will list the available ligands adhering
to the provided input. By clicking on the selected ligand name users will be redirected to that specific
ligand info page.


Ligand Info page
----------------

The ligand info page can be accessed directly by a ligand query or from the results page of the above ligand browser.
The top of the ligand info page displays information about ligand structure (2D image, SMILES, InChI key),
names (common, and chemical names, and aliases), physicochemical properties (molecular weight, logP and counts
for hydrogen bond acceptors/donors, and rotatable bonds), molecule type (small molecule/peptide/protein, drug status
and endogenous/surrogate), and database links (internal and external). For ligands that have this information,
two additional boxes provide GPCR-ligand crystal/cryo-EM structure complexes and mutations affecting ligand activity.
The bottom of the page shows bioactivities for the given ligand across receptor targets.
The bioactivity browser allows filtering by the receptor classification, bioactivity, and source database.
The information on endogenous ligands and target FDA approval status have been derived from Guide to Pharmacology
and DrugBank databases, respectively.


Endogenous ligand browser
-------------------------

The endogenous ligand-GPCR system spans different relationships ranging (ligand:receptor) 1:1,
1:many, many:1 and many:many relationships. To facilitate browsing across either ligands or receptors, we
developed an endogenous ligand browser. This browser contains data for 543 distinct endogenous ligands for
253 human GPCRs, and 157 mouse, rat, or guinea pig receptors. For each receptor, alternative endogenous ligands are
classified as principal or secondary, as defined by the nomenclature committee of the `International Union of Basic and Clinical Pharmacology`_
and have an additional ranking by potency. For ligand-receptor pairs with multiple potency (pEC50) or affinity (pKi) values,
the browser provides minimum, mean and maximum values, with grayscale background aiding comparison. Finally, the
browser contains information about the ligand type, ligand name with a direct link to the ligand info page in GPCRdb,
receptor information as family, species, IUPHAR and UniProt name and a popup showing the original references for bioactivities.

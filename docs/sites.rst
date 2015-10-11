Sites
=================

Ligand interactions
-------------------

The ligand interaction workflow allow a user to upload a PDB file and get an analysis of protein-ligand interactions
in the complex.

Site search - manual
--------------------

The site search tool allows a user to search a set of receptors for a sequence motif consisting of residue
positions and chemical properties. Using the tools is a two step process.

1.  The user is first presented with a receptor selection page. Receptors can be selected individually or by family.
    The user can select as many receptors as he/she wishes (WARNING: selecting a large number of receptors increases
    loading time).

2.  After receptors have been selected, the user is presented with a sequence motif selecetion page. Site residues
    should be selected individually. Clicking the down arrow button next to a sequence segment will expand the residues
    within that segment. Chemical features (Hydrophobic, hydrogen bond donor, etc.) should then be selected for each
    motif residue. When a feature has been selected, a list of amino acids that match the feature will appear to the
    right of the residue.

    The selected residues can be organised into separate interactions. An interaction can contain one or more residues.
    To add an interaction, click the 'Add interaction' button. Selected residues will be added to the currently active
    interaction (shown in bold text). To change the active interaction, click on the name of the interaction. Within an
    interaction, the number of residues required to match can be specified in the 'Min. match' selection box.

After completing these two steps, an alignment is displayed. The sequences of the selected receptors are split into
"Matching sequences" and "Non-matching sequences", according to their match of the selected site. To display the
sequence number of an aligned residue, as well as generic number indices, hover the mouse over it.

Site search - from pdb complex
------------------------------

This is a variant of the manual site search tool, where the user can upload a PDB structure and have protein-ligand
interactions automatically detected and translated into a site search. After interactions have been detected, the user
can edit the definition, and continue as in a manual search.

Pharmacophore generation
------------------------

The tool is based on the following paper:

K Fidom, V Isberg, A Hauser, S Mordalski, T Lehto, AJ Bojarski, DE Gloriam, "A New Crystal Structure Fragment-Based
Pharmacophore Method for G Protein-Coupled Receptors", **2015**, *Methods*, 71, 104–112. `10.1016/j.ymeth.2014.09.009`_

.. _10.1016/j.ymeth.2014.09.009: http://dx.doi.org/10.1016/j.ymeth.2014.09.009

Abstract
^^^^^^^^

We have developed a new method for the building of pharmacophores for G protein-coupled receptors, a major drug target
family. The method is a combination of the ligand- and target-based pharmacophore methods and founded on the extraction
of structural fragments, interacting ligand moiety and receptor residue pairs, from crystal structure complexes. We
describe the procedure to collect a library with more than 250 fragments covering 29 residue positions within the
generic transmembrane binding pocket. We describe how the library fragments are recombined and inferred to build
pharmacophores for new targets. A validating retrospective virtual screening of histamine H1 and H3 receptor
pharmacophores yielded area-under-the-curves of 0.88 and 0.82, respectively. The fragment-based method has the unique
advantage that it can be applied to targets for which no (homologous) crystal structures or ligands are known. 47% of
the class A G protein-coupled receptors can be targeted with at least four-element pharmacophores. The fragment
libraries can also be used to grow known ligands or for rotamer refinement of homology models. Researchers can download
the complete fragment library or a subset matching their receptor of interest using our new tool in GPCRdb.

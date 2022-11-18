Welcome to the GPCRdb documentation
===================================

The GPCRdb contains data, diagrams and web tools for G protein-coupled receptors (GPCRs).
Users can browse all GPCR crystal structures and the largest collection of receptor mutants.
Diagrams can be produced and downloaded to illustrate receptor residues (snake-plot and helix box diagrams) and
relationships (phylogenetic trees). Reference (crystal) structure-based sequence alignments take into account helix
bulges and constrictions, display statistics of amino acid conservation and have been assigned generic
residue numbering for equivalent residues in different receptors.

The `source code`_ and `source data`_ are freely available on `GitHub`_.

Below, a table overview of all the different pages and functionalities in GPCRdb grouped by sections, along links to specific documentation pages, associated slides and video demonstrations.

.. _source code: https://github.com/protwis/protwis
.. _source data: https://github.com/protwis/gpcrdb_data
.. _GitHub: https://github.com
.. _Isberg et al. Nucleic Acids Research 2014: https://doi.org/10.1093/nar/gkt1255
.. _Isberg et al. Nucleic Acids Research 2016: https://doi.org/10.1093/nar/gkv1178
.. _Pándy-Szekeres et al. Nucleic Acids Research 2018: https://doi.org/10.1093/nar/gkx1109
.. _Kooistra et al. Nucleic Acids Research 2021: https://doi.org/10.1093/NAR/GKAA1080
.. _Pándy-Szekeres et al. Nucleic Acids Research 2023: https://doi.org/10.1093/nar/gkac1013
.. _Isberg et al. Trends in Pharmacological Sciences 2015: https://doi.org/10.1016/j.tips.2014.11.001
.. _Hauser et al. Cell 2018: https://doi.org/10.1016/j.cell.2017.11.033
.. _Marti-Solano et al. Nature 2020: https://doi.org/10.1038/s41586-020-2888-2
.. _Munk et al. British Journal of Pharmacology 2016: https://doi.org/10.1111/bph.13509
.. _Kooistra et al. Nature Structural Molecular Biology 2021: https://doi.org/10.1038/s41594-021-00675-6
.. _Munk et al. Nature Methods 2019: https://doi.org/10.1038/s41592-018-0302-x
.. _Hauser et al. Nature Reviews Drug Discovery 2017: https://doi.org/10.1038/nrd.2017.178
.. _Munk et al. Current Opinion in Pharmacology 2016: https://doi.org/10.1016/j.coph.2016.07.003
.. _Mutations Video: https://www.youtube.com/watch?v=XU9CnFuKDqk
.. _Receptor page Video: https://www.youtube.com/watch?v=LGq73spAZhc
.. _Receptor similarity Video: https://www.youtube.com/watch?v=_JYqES3B0yU
.. _Sequence alignment Video: https://www.youtube.com/watch?v=jxdrCKsXA4M
.. _Structure comparison tool Video: https://www.youtube.com/watch?v=RGGDyuLywZY
.. _Structure similarity trees Video: https://www.youtube.com/watch?v=Fv9MWWe9GEU


Below, a table overview of all the different pages and functionalities in GPCRdb grouped by sections,
along links to specific documentation pages, associated slides and video demonstrations.


.. csv-table:: **SEQUENCES**
   :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
   :widths: 25 25 25 25 25 25 25

   "Sequence alignments", "Provides sequence alignments analyses of receptors, either full sequence of segments of interest.", ":ref:`Sequences:Structure-based alignments`", "-", "-", "`Sequence alignment Video`_", "`Isberg et al. Nucleic Acids Research 2016`_, `Kooistra et al. Nucleic Acids Research 2021`_"
   "Generic residue number tables", "Displays the generic residue number tables for the single or set of receptors selected.", ":ref:`Generic residue numbering`", "-", "-", "-", "`Isberg et al. Trends in pharmacological Sciences 2015`_"
   "Genetic variants", "Section showing the variation coverage, single receptor variants and the estimated economic burden for drugs targeting GPCRs", ":ref:`Genetic variants`", "-", "-", "-", "`Hauser et al. Cell 2018`_"
   "Isoforms", "Info page highlighting the number of unique isoforms detected for each receptor gene", "", "-", "-", "-", "`Marti-Solano et al. Nature 2020`_"

.. csv-table:: **SEQUENCE ANALYSIS**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "Receptor similarity", "Section showcasing receptor similarities using BLAST alignment searches, phylogenetic trees or all-to-all matrix comparisons.", ":ref:`Sequences:Similarity search - BLAST`", "-", "-", "`Receptor similarity Video`_", "`Isberg et al. Nucleic Acids Research 2016`_, `Munk et al. British Journal of Pharmacology 2016`_"
  "Site search (by seq motif.)", "-", "-", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_"

.. csv-table:: **STRUCTURES**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "Structure coverage", "Overview of the structure information available in GPCRdb. Data is shown using detailed inforgraphics and plots.", ":ref:`Structures`", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_"
  "Structures", "Browser page listing detailed information for all the structures present in GPCRdb and their external references.", ":ref:`Structures:Structure browser`", "-", "-", "-", "`Isberg et al. Nucleic Acids Research, 2014`_, `Kooistra et al. Nucleic Acids Research 2021`_"
  "Structure models", "Browser page listing all the AlphaFold generated homology models present in GPCRdb, with their original associate template. ", ":ref:`Structures:Structure models`", "-", "-", "-", "`Pándy-Szekeres et al. Nucleic Acids Research 2023`_"
  "Structure model validation", "Browser page listing the RMSD values comparing the latest model before a structure of the same receptor in the same state was published.", "-", "-", "-", "-", "`Kooistra et al. Nucleic Acids Research 2021`_, `Pándy-Szekeres et al. Nucleic Acids Research 2023`_"

.. csv-table:: **STRUCTURE ANALYSIS**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "Structure comparison tool", "Interactive tool for investigation of single structures or comparison of sets of structures. The tool allow for more than 20 different plot representations and lists available contact position pairs. ", ":ref:`Structure comparison:Structure comparison tool`", "-", "-", "`Structure comparison tool Video`_", "`Kooistra et al. Nature Structural Molecular Biology 2021`_"
  "Structure similarity trees", "Interactive tool showcasing the similarity trees of selected set of receptors. Generated trees can be further graphically tweaked and downloaded in high resolution format. ", ":ref:`Structure comparison:Structure similarity trees`", "-", "-", "`Structure similarity trees Video`_", "`Kooistra et al. Nature Structural Molecular Biology 2021`_"
  "Structure superposition", "Functionality designed for the superimposition of user defined structures (reference and test), allowing analysis for full structures or segment based.", ":ref:`Structure comparison:Structure superposition`", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_"
  "Generic residue numbering (PDB)", "Functionality for the annotation using generic numbers from GPCRdb of user uploaded PDB files.", ":ref:`Structure comparison:Generic residue numbering (PDB)`", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_, `Isberg et al. Trends in pharmacological Sciences 2015`_"

.. csv-table:: **STRUCTURE CONSTRUCTS**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "Construct/Experiment design", "Section for the design and alignment of experimental constructs, and associated browser page listing experiments walkthrough.", ":ref:`Structure constructs`", "-", "-", "-", "`Munk et al. Nature Methods 2019`_"
  "Truncation/Fusion analysis", "Section with pages showing information about truncation sites, fusion sites and deletion loops across the available GPCRdb data.", ":ref:`Structure constructs:Truncation & Fusion analysis`", "-", "-", "-", "`Munk et al. Nature Methods 2019`_"
  "Mutation analysis", "Section with mutations oriented browsers, listing stabilizing mutations, substitution matrix and a dedicated stabilising mutation analyser.", ":ref:`Structure constructs:Mutation analysis`", "-", "-", "-", "`Munk et al. Nature Methods 2019`_"

.. csv-table:: **DETERMINANTS & MUTATIONS**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "Sequence signature tool", "Interactive tool for the investigation of sequence signature across two different user defined set of receptors.", ":ref:`Sequence signature tool`", "-", "-", "-", "`Kooistra et al. Nucleic Acids Research 2021`_"
  "State stabilizing mutation design", "Browser page listing detailed state stabilising mutation information for each receptor present in GPCRdb, after user selection.", "-", "-", "-", "-", "`Kooistra et al. Nature Structural Molecular Biology 2021`_"

.. csv-table:: **LIGANDS & BIOACTIVITIES**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "Ligand coverage", "Overview of the ligands information available in GPCRdb. Data is shown using detailed inforgraphics and plots.", "-", "-", "-", "-", "`Pándy-Szekeres et al. Nucleic Acids Research 2018`_"
  "Ligands (ChEMBL, GtP, Ki db)", "Section allowing the search for ligands associated to a specific receptor or using ligand name, database ID or chemical information (SMILES or Inchikey).", "-", "-", "-", "-", "`Pándy-Szekeres et al. Nucleic Acids Research 2018`_, `Pándy-Szekeres et al. Nucleic Acids Research 2023`_"

.. csv-table:: **ENDOGENOUS LIGANDS**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "Endogenous ligands (GtP)" , "Browser page listing detailed information for endogenous ligands present in GPCRdb. Data are derived and maintained by Guide to Pharmacology.", "-", "-", "-", "-", "`Pándy-Szekeres et al. Nucleic Acids Research 2023`_"

.. csv-table:: **DRUGS & AGENTS IN TRIAL**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "Drugs, targets & indicators", "Browser page listing information about drugs, their targets of action, therapeutic indication and clinical status, with associated references.", ":ref:`Drugs:Drug browser`", "-", "-", "-", "`Hauser et al. Nature Reviews Drug Discovery 2017`_"
  "Drug target tree", "Interactive infographic tree showing drug data information on established or under clinical trials GPCR targets.", ":ref:`Drugs:Drug target mapping`", "-", "-", "-", "`Hauser et al. Nature Reviews Drug Discovery 2017`_"
  "Drug statistics", "Overview of the GPCR class as drug target, with focus on receptor family targets, drug molecule types, mode of action and disease indications.", ":ref:`Drugs:Drug statistics`", "-", "-", "-", "`Hauser et al. Nature Reviews Drug Discovery 2017`_"

.. csv-table:: **LIGAND SITES**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "GPCR-ligand interactions", "Functionality showing the protein-ligand interactions for the available PDB structures in GPCRdb using graphical representation and 3D visualization tools.", ":ref:`Sites:Ligand interactions`", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_, `Munk et al. Current Opinion in Pharmacology 2016`_"
  "Site search", "Section designed for the investigation of protein-ligand interactions of set of receptors, either using sequence motifs or ligand complex though a user defined PDB file.", ":ref:`Sites:Site search - from PDB complex`", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_"

.. csv-table:: **LIGAND SITE MUTATIONS**
  :header:  "Page name", "Short description", "Text", "Video", "Slides", "Demo", "Reference"
  :widths: 25 25 25 25 25 25 25

  "Mutation coverage", "Overview of the mutations information available in GPCRdb. Data is shown using detailed inforgraphics.", ":ref:`Mutations`", "-", "-", "-", "`Munk et al. Current Opinion in Pharmacology 2016`_"
  "Mutations", "Browser page listing mutations for user selected receptors and protein segments. Result tables also provides information about ligand affinity for the mutation (FoldChange) if available.", ":ref:`Mutations:Mutations browser`", "-", "-", "`Mutations Video`_", "`Munk et al. Current Opinion in Pharmacology 2016`_"
  "Mutation design tool", "Section with mutation design tool based either on a PDB code or receptor name. Result page lists suggested mutations with associated structure interactions, supporting ligands, receptors and mutagenesis experiments.", ":ref:`Mutations`", "-", "-", "-", "`Munk et al. Current Opinion in Pharmacology 2016`_"
  "Mutation data submission", "Description to the mutation data submission form and guidelines on how to submit your experimental data to GPCRdb.", ":ref:`Mutations:Mutation data submission`", "-", "-", "-", "`Munk et al. Current Opinion in Pharmacology 2016`_"


The documentation is organised into three sections:

* :ref:`user-docs`
* :ref:`dev-docs`
* :ref:`about-docs`

.. _user-docs:

.. toctree::
    :maxdepth: 2
    :caption: User documentation

    receptors
    signalproteins
    sequences
    sequence_signature
    structures
    structure_comparison
    constructs
    mutations
    biasedsignaling
    sites
    generic_numbering
    drugs
    nhs
    variants

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
    contributors
    citing
    acknowledgements
    legal_notice
    meetings
    linking
    external_sites

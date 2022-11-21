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


.. |Mutations Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                     :target: https://www.youtube.com/watch?v=XU9CnFuKDqk
.. |Receptor page Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                         :target: https://www.youtube.com/watch?v=LGq73spAZhc
.. |Receptor similarity Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                               :target: https://www.youtube.com/watch?v=_JYqES3B0yU
.. |Sequence alignment Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                              :target: https://www.youtube.com/watch?v=jxdrCKsXA4M
.. |Structure comparison tool Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                                     :target: https://www.youtube.com/watch?v=RGGDyuLywZY
.. |Structure similarity trees Video| image:: https://justbewell.info/wp-content/uploads/2020/02/yt.png
                                      :target: https://www.youtube.com/watch?v=Fv9MWWe9GEU

.. _Sequence alignments: https://docs.gpcrdb.org/sequences.html#structure-based-alignments
.. _Generic residue number tables: https://docs.gpcrdb.org/generic_numbering.html#generic-residue-numbering
.. _Genetic variants: https://docs.gpcrdb.org/variants.html#genetic-variants
.. _Receptor similarity: https://docs.gpcrdb.org/sequences.html#similarity-search-gpcrdb
.. _Structure coverage: https://docs.gpcrdb.org/structures.html#structures
.. _Structures: https://docs.gpcrdb.org/structures.html#structure-browser
.. _Structure models: https://docs.gpcrdb.org/structures.html#structure-models
.. _Structure comparison tool: https://docs.gpcrdb.org/structure_comparison.html#structure-comparison-tool
.. _Structure similarity trees: https://docs.gpcrdb.org/structure_comparison.html#structure-similarity-trees
.. _Structure superposition: https://docs.gpcrdb.org/structure_comparison.html#structure-superposition
.. _Generic residue numbering (PDB): https://docs.gpcrdb.org/structure_comparison.html#generic-residue-numbering-pdb
.. _Construct/Experiment design: https://docs.gpcrdb.org/constructs.html#structure-constructs
.. _Truncation/Fusion analysis: https://docs.gpcrdb.org/constructs.html#truncation-fusion-analysis
.. _Mutation analysis: https://docs.gpcrdb.org/constructs.html#mutation-analysis
.. _Sequence signature tool: https://docs.gpcrdb.org/sequence_signature.html#sequence-signature-tool
.. _Drugs targets and indicators: https://docs.gpcrdb.org/drugs.html#drug-browser
.. _Drug target tree: https://docs.gpcrdb.org/drugs.html#drug-target-mapping
.. _Drug statistics: https://docs.gpcrdb.org/drugs.html#drug-statistics
.. _GPCR-ligand interactions: https://docs.gpcrdb.org/sites.html#ligand-interactions
.. _Site search: https://docs.gpcrdb.org/sites.html#site-search-from-pdb-complex
.. _Mutation coverage: https://docs.gpcrdb.org/mutations.html#mutations
.. _Mutations: https://docs.gpcrdb.org/mutations.html#mutation-browser
.. _Mutation design tool: https://docs.gpcrdb.org/mutations.html#mutation-browser
.. _Mutation data submission: https://docs.gpcrdb.org/mutations.html#mutation-data-submission

Below, a table overview of all the different pages and functionalities in GPCRdb grouped by sections,
along links to specific documentation pages, associated slides and video demonstrations.


.. csv-table:: **SEQUENCES**
   :header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
   :widths: 25 25 25 25 25 25

   "`Sequence alignments`_", "-", "-", "|Sequence alignment Video|", "`Isberg et al. Nucleic Acids Research 2016`_, `Kooistra et al. Nucleic Acids Research 2021`_", "Provides sequence alignments analyses of receptors, either full sequence of segments of interest."
   "`Generic residue number tables`_", "-", "-", "-", "`Isberg et al. Trends in pharmacological Sciences 2015`_", "Displays the generic residue number tables for the single or set of receptors selected."
   "`Genetic variants`_", "-", "-", "-", "`Hauser et al. Cell 2018`_", "Section showing the variation coverage, single receptor variants and the estimated economic burden for drugs targeting GPCRs"
   "Isoforms", "-", "-", "-", "`Marti-Solano et al. Nature 2020`_", "Info page highlighting the number of unique isoforms detected for each receptor gene"

.. csv-table:: **SEQUENCE ANALYSIS**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "`Receptor similarity`_", "-", "-", "|Receptor similarity Video|", "`Isberg et al. Nucleic Acids Research 2016`_, `Munk et al. British Journal of Pharmacology 2016`_", "Section showcasing receptor similarities using BLAST alignment searches, phylogenetic trees or all-to-all matrix comparisons."
  "Site search (by seq motif.)", "-", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_", "-"

.. csv-table:: **STRUCTURES**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "`Structure coverage`_", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_", "Overview of the structure information available in GPCRdb. Data is shown using detailed inforgraphics and plots."
  "`Structures`_", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2014`_, `Kooistra et al. Nucleic Acids Research 2021`_", "Browser page listing detailed information for all the structures present in GPCRdb and their external references."
  "`Structure models`_", "-", "-", "-", "`Pándy-Szekeres et al. Nucleic Acids Research 2023`_", "Browser page listing all the AlphaFold generated homology models present in GPCRdb, with their original associate template. "
  "Structure model validation", "-", "-", "-", "`Kooistra et al. Nucleic Acids Research 2021`_, `Pándy-Szekeres et al. Nucleic Acids Research 2023`_", "Browser page listing the RMSD values comparing the latest model before a structure of the same receptor in the same state was published."

.. csv-table:: **STRUCTURE ANALYSIS**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "`Structure comparison tool`_", "-", "-", "|Structure comparison tool Video|", "`Kooistra et al. Nature Structural Molecular Biology 2021`_", "Interactive tool for investigation of single structures or comparison of sets of structures. The tool allow for more than 20 different plot representations and lists available contact position pairs. "
  "`Structure similarity trees`_", "-", "-", "|Structure similarity trees Video|", "`Kooistra et al. Nature Structural Molecular Biology 2021`_", "Interactive tool showcasing the similarity trees of selected set of receptors. Generated trees can be further graphically tweaked and downloaded in high resolution format. "
  "`Structure superposition`_", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_", "Functionality designed for the superimposition of user defined structures (reference and test), allowing analysis for full structures or segment based."
  "`Generic residue numbering (PDB)`_", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_, `Isberg et al. Trends in pharmacological Sciences 2015`_", "Functionality for the annotation using generic numbers from GPCRdb of user uploaded PDB files."

.. csv-table:: **STRUCTURE CONSTRUCTS**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "`Construct/Experiment design`_", "-", "-", "-", "`Munk et al. Nature Methods 2019`_", "Section for the design and alignment of experimental constructs, and associated browser page listing experiments walkthrough."
  "`Truncation/Fusion analysis`_", "-", "-", "-", "`Munk et al. Nature Methods 2019`_", "Section with pages showing information about truncation sites, fusion sites and deletion loops across the available GPCRdb data."
  "`Mutation analysis`_", "-", "-", "-", "`Munk et al. Nature Methods 2019`_", "Section with mutations oriented browsers, listing stabilizing mutations, substitution matrix and a dedicated stabilising mutation analyser."

.. csv-table:: **DETERMINANTS & MUTATIONS**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "`Sequence signature tool`_", "-", "-", "-", "`Kooistra et al. Nucleic Acids Research 2021`_", "Interactive tool for the investigation of sequence signature across two different user defined set of receptors.""
  "State stabilizing mutation design", "-", "-", "-", "`Kooistra et al. Nature Structural Molecular Biology 2021`_", "Browser page listing detailed state stabilising mutation information for each receptor present in GPCRdb, after user selection."

.. csv-table:: **LIGANDS & BIOACTIVITIES**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "Ligand coverage", "-", "-", "-", "`Pándy-Szekeres et al. Nucleic Acids Research 2018`_", "Overview of the ligands information available in GPCRdb. Data is shown using detailed inforgraphics and plots."
  "Ligands (ChEMBL, GtP, Ki db)", "-", "-", "-", "`Pándy-Szekeres et al. Nucleic Acids Research 2018`_, `Pándy-Szekeres et al. Nucleic Acids Research 2023`_", "Section allowing the search for ligands associated to a specific receptor or using ligand name, database ID or chemical information (SMILES or Inchikey)."

.. csv-table:: **ENDOGENOUS LIGANDS**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "Endogenous ligands (GtP)" , "-", "-", "-", "`Pándy-Szekeres et al. Nucleic Acids Research 2023`_", "Browser page listing detailed information for endogenous ligands present in GPCRdb. Data are derived and maintained by Guide to Pharmacology."

.. csv-table:: **DRUGS & AGENTS IN TRIAL**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "`Drugs targets and indicators`_", "-", "-", "-", "`Hauser et al. Nature Reviews Drug Discovery 2017`_", "Browser page listing information about drugs, their targets of action, therapeutic indication and clinical status, with associated references."
  "`Drug target tree`_", "-", "-", "-", "`Hauser et al. Nature Reviews Drug Discovery 2017`_", "Interactive infographic tree showing drug data information on established or under clinical trials GPCR targets."
  "`Drug statistics`_", "-", "-", "-", "`Hauser et al. Nature Reviews Drug Discovery 2017`_", "Overview of the GPCR class as drug target, with focus on receptor family targets, drug molecule types, mode of action and disease indications."

.. csv-table:: **LIGAND SITES**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "`GPCR-ligand interactions`_", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_, `Munk et al. Current Opinion in Pharmacology 2016`_", "Functionality showing the protein-ligand interactions for the available PDB structures in GPCRdb using graphical representation and 3D visualization tools."
  "`Site search`_", "-", "-", "-", "`Isberg et al. Nucleic Acids Research 2016`_", "Section designed for the investigation of protein-ligand interactions of set of receptors, either using sequence motifs or ligand complex though a user defined PDB file."

.. csv-table:: **LIGAND SITE MUTATIONS**
:header:  "Page name", "Video", "Slides", "Demo", "Reference", "Short description"
:widths: 25 25 25 25 25 25

  "`Mutation coverage`_", "-", "-", "-", "`Munk et al. Current Opinion in Pharmacology 2016`_", "Overview of the mutations information available in GPCRdb. Data is shown using detailed inforgraphics."
  "`Mutations`_", "-", "-", "|Mutations Video|", "`Munk et al. Current Opinion in Pharmacology 2016`_",  "Browser page listing mutations for user selected receptors and protein segments. Result tables also provides information about ligand affinity for the mutation (FoldChange) if available."
  "`Mutation design tool`_", "-", "-", "-", "`Munk et al. Current Opinion in Pharmacology 2016`_", "Section with mutation design tool based either on a PDB code or receptor name. Result page lists suggested mutations with associated structure interactions, supporting ligands, receptors and mutagenesis experiments."
  "`Mutation data submission`_", "-", "-", "-", "`Munk et al. Current Opinion in Pharmacology 2016`_", "Description to the mutation data submission form and guidelines on how to submit your experimental data to GPCRdb."


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

Sequences
=========

Structure-based alignments
--------------------------

The "Structure-based alignments" tool allows for alignment of user selected receptors and sequence segments.
Using the tool is a two step process.

1.  The user is first presented with a receptor selection page. Receptors can be selected individually or by family.
    The user can select as many receptors as he/she wishes (WARNING: selecting a large number of receptors increases
    loading time).
2.  After receptors have been selected, the user is presented with a sequence segment selection page. The user can
    select one or more sequence segments, and/or expand each segment to select the residues within it individually.
    Residues selected individually are grouped into a custom sequence segment.

After completing these two steps, an alignment is displayed. To display the sequence number of an aligned residue, as
well as generic numbers, hover the mouse over it. At the bottom of the page, a consensus sequence as well as
conservation statistics for amino acids and chemical features are displayed.

Phylogeneric trees
------------------

The phylogenetic tree tool allows for generation of phylogenetic trees based on user selected receptors and sequence
segments. Using the tool is a three step process.

1.  The user is first presented with a receptor selection page. Receptors can be selected individually or by family.
    The user can select as many receptors as he/she wishes (WARNING: selecting a large number of receptors increases
    loading time).
2.  After receptors have been selected, the user is presented with a sequence segment selection page. The user can
    select one or more sequence segments, and/or expand each segment to select the residues within it individually.
    Residues selected individually are grouped into a custom sequence segment.
3.  In the third step, a settings page is displayed. The amount of bootstrapping replicas (0, 10 or 100) and the type
    of tree (rectangular or circular) are configurable by the user. User are also offered an option to show branch
    lengths that represent the evolutionary distance between the nodes, or show the same branch length between every
    node.

To view an alignment of the sequences used to generate the tree after it has been displayed, click the "View alignment"
button.

The trees are generated using `PHYLIP`_ and `jsPhyloSVG`_.

.. _PHYLIP: http://evolution.genetics.washington.edu/phylip.html
.. _jsPhyloSVG: http://www.jsphylosvg.com/

Similarity search - GPCRdb
--------------------------

The GPCRdb similarity search tools allows a user to find the most similar receptors for a reference sequence, out of 
all GPCRs, or a subset selected by the user. The tools is more accurate than BLAST search, since it uses curated,
structure-based alignments, but only works on sequences that are already in the database. Using the tool is a three
step process.

1.  The user is first presented with a reference receptor selection page.
2.  Once a reference receptor has been selected, the user is presented with a sequence segment selection page. The user
    can select one or more sequence segments, and/or expand each segment to select the residues within it individually. 
    Residues selected individually are grouped into a custom sequence segment.
3.  The third step is selecting a comparison receptor set. The selected receptors will be compared to the reference
    receptor based on the selected sequence segments, and their similarities computed. The user can select as many
    receptors as he/she wishes (WARNING: selecting a large number of receptors increases loading time).

After completing these three steps, an alignment is displayed, with the receptors in the comparison set ranked by
similarity to the reference receptor. The three columns to the right of the receptor ID show three computed properties:

* **Sequence identity (%I)**: The percentage of identical amino acids.
* **Sequence similarity (%S)**: The percentage of similar amino acids (where similar is defined as BLOSUM62 score > 0).
* **Similarity score (S)**: The sum of every position's BLOSUM62 score.

To display the sequence number of an aligned residue, as well as generic number indices, hover the mouse over it.

Similarity search - BLAST
-------------------------

The BLAST based similarity search is an alternative to the GPCRdb similarity search that works for any user submitted
sequence (the query sequence does not have to be in GPCRdb already). The runs a standard BLAST search on a custom
BLAST database that contains every sequence from GPCRdb.

The results page show a list of the best BLAST hits for the submitted query sequence.

Similarity matrix
-----------------

The similarity matrix tool allows a user to quickly gain an overview of the sequence identity and similarity between
all sequences in a receptor family, or a custom selected group of receptors. Using the tool is a two step process.

1.  The user is first presented with a receptor selection page. Receptors can be selected individually or by family.
    The user can select as many receptors as he/she wishes (WARNING: selecting a large number of receptors increases
    loading time).
2.  After receptors have been selected, the user is presented with a sequence segment selection page. The user can
    select one or more sequence segments, and/or expand each segment to select the residues within it individually.
    Residues selected individually are grouped into a custom sequence segment.

The results are shown as a table of identities and similarites, color-coded in a red-yellow-green color scale ranging
from low to high identity/similarity. Identities are shown in the lower-left half of the table, and similarites in the
upper-right half.
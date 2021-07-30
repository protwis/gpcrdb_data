Structure comparison
====================

Structure comparison tool
-------------------------

The Structure comparison tool allows users to perform powerful analyses of a structure, a set of structures, or even compare two (sets of) structures. When opening op the tool, there are three tabs displayed at the top. Depending on what analysis one wants to perform, one has to choose one of the three:

#. Single structure
	Utilize this tab, when you want to investigate the interactions and properties of a single structure. Click on the *Select Structure* button, select a structure in the list (by ticking the leftmost checkbox, by clicking on a row, or by importing the PDB code at the top) and close the structure selection panel. Then press the green *Go* button and the structure will be analyzed. Optionally, you can adjust the configuration of the tool by clicking on the cogwheel icon before pressing *Go*.
	
#. Single set of structures
	Utilize this tab, when you want to investigate variations of interactions, distances, and properties of a set of structures. Click on the *Select Structures* button, select the structures in the list (by ticking the leftmost checkbox, by clicking on a row, or by importing the PDB codes at the top) and close the structure selection panel. Then press the green *Go* button and the structure set will be analyzed. Optionally, you can adjust the configuration of the tool by clicking on the cogwheel icon before pressing *Go*.

#. Two sets of structures
	Utilize this tab, when you want to investigate the different or shared interactions, distances, and properties of two sets of structures. First click on the *Select (Set 1)* button, select the structures in the list (by ticking the leftmost checkbox, by clicking on a row, or by importing the PDB codes at the top) and close the structure selection panel. Subsequently, click on the *Select (Set 2)* button. Then press the green *Go* button and the selected structure sets will be analyzed. Optionally, you can adjust the configuration of the tool by clicking on the cogwheel icon before pressing *Go*.

After selecting the structures and pressing the *Go* button, the tool analyzes the structures and collects the data from the analysis, this might take a minute. When completed the gray overlay will disappear and the three plotting panels in the middle of the screen and the data browsers at the bottom are populated. The analyzed data itself is presented in interactive browsers at the bottom in four different tabs:

#. Contact position pairs
	All data relating to the residue-residue pairs that interact in the selected structure(s). This data ranges from interaction frequencies per interaction type to distances, angles, to sequence conservation. It should be noted that filtering action in this browser will impact several of the plotting options that are discussed below. For example, when showing the 3D structure and then filtering on a column, only those interactions will be shown in the 3D structure or flare plot that are also still displayed in this browser, all other interactions will be filtered out.

#. Contact position-AA pairs
	This browser is an extension of the first browser. Instead of grouping all interaction frequencies for each residue pair, it first groups on unique amino acid pairs and then analyzes the interaction frequencies and sequence conservation for that specific pair of amino acids. This tab can, for example, be used to figure out if a conserved interaction in one structure set is due to the conservation of a specific amino acid pair that is not conserved in the other structure set.
	
#. Residue backbone & sidechain movement
	In contrast to the first two browsers, the last two browsers focus on each individual residue with a generic residue number. In this browser, multiple properties are analyzed for each individual residue, such as the rotamer angle, (relative) solvent-accessible surface area (SASA and RSA), sequence conservation, and distances. This browser can, for example, be used to identify movements in the backbone and sidechain of specific residues.
		
#. Residue helix types, bulges, and constrictions
	The last of the browsers also focuses on each individual residue with a generic residue number. In contrast to the previous browser, this one focuses mainly on the backbone conformation and secondary structure described at each of the residues using the secondary structure annotation, tau and theta angles, phi/psi/tau dihedrals, and is complemented again by sequence conservation. If backbone variations occur, this is the browser to identify them in, such as - for example - the constriction at the end of TM7 upon activation.
	
Finally, in the middle the data can be visualized in a plethora of different ways:

* TM1-7 segment movement
	* Extracellular - Segment plot (2D and 3D)
		A 2D or 3D depiction of the movement and rotation of the seven TM helices at the extracellular ends when comparing two different structure sets. The movements are based for each helix, on the most-extracellular three residues with a generic residue number that are present in all structures in both sets.
	* Middle of membrane - Segment plot (2D and 3D)
		A 2D or 3D depiction of the movement and rotation of the seven TM helices at the middle of the membrane (based on the `OPM`_ orientation of the GPCR in the membrane) when comparing two different structure sets.
	* Cytosolic - Segment plot (2D and 3D)
		A 2D or 3D depiction of the movement and rotation of the seven TM helices at the intracellular ends when comparing two different structure sets. The movements are based for each helix, on the most-intracellular three residues with a generic residue number that are present in all structures in both sets.

* Contacts between generic residue positions
	* Flare plot ‡
		A GPCRdb-customized version of the flare plot that depicts interacting residues in a circular fashion. With the default enabled option to show interactions between residues from consecutive segments on the outside of the circle and all other interactions on the inside of the circle. For a single structure, the line colors depict the interaction type, for a single set of structures the frequency of interactions for a given residue-residue pair, and for two sets of structures the difference in interaction frequency between the two sets for a given residue-residue pair. 
	* Heatmap ‡
		A heatmap of all residues-against-all-residues depicting all interactions observed in the selected structure(s). For a single structure, the colors depict the interaction type, for a single set of structures the frequency of interactions for a given residue-residue pair, and for two sets of structures the difference in interaction frequency between the two sets for a given residue-residue pair. 
	* Network (2D and 3D) ‡
		These plots show in 2D or 3D how the interacting residues are interconnected in (sets of) connected subnetworks. When right clicking on a specific subnetwork, the plot zooms in on that specific network and by right clicking again it will go back to the full overview. 
	* Structure (3D) ‡
		This plot uses the `NGL`_ molecular viewer to show the structure(s) and interaction that are observed between the residue pairs. This viewer is again based on the data shown in first data browser (see above) and interactively changes whenever a filter is applied (or removed) in this data browser.
* Contacts between segments (TM1-7, H8 & loops)
	* Flare plot (segments) ‡
		This option shows flare plots highlighting the number of shared interactions between the structural segments instead of residues. The structural segments are defined as the seven transmembrane helices, helix 8, and the loop regions.
	* Network (2D and 3D) ‡
		This option, shows 2D or 3D networks highlighting the number of shared interactions between the structural segments instead of residues. The structural segments are defined as the seven transmembrane helices, helix 8 and the loop regions.
* Contacts frequencies
	* Box plot ‡ 
		A plotting option that shows the interaction frequency differences when comparing two sets of structures. 
* Residue properties
	* Box plot (distribution) ‡ 
		A plotting option that shows the distribution for the different residue properties when comparing two sets of structures. 
	* Heatmap (distance)
		This heatmap shows the overall distance (single structure or single set of structures) or change in distance for residue-residue pairs based on the Cα distance pairs. 
	* Scatter plot (correlation) ‡ 
		Scatter plotting option that allows for the selection of different types of residue properties and maps them against each other to find a correlation.
	* Snakeplot (2D, topology) ‡ 
		A highly interactive and customizable version of the well-known snake plot that can be used to map any of the structural properties on to the snakeplot and 
	* Structure (3D, movement)
		In the NGL viewer the overall normalized distance changes between two sets of structures are depicted based on the all-against-all Cα distance pairs. The red-white-blue color gradient used on the structure shows where overall an increase or decrease in placement (based on all distances to that specific residue) has been observed.

‡ These plots are based on the data shown in the first data browser (see above) and will therefore change when it is redrawn after a filter is applied or removed in this data browser.

For more information about the different properties that are used in this tool, please check out the preprint describing the `Structure analysis platform <https://doi.org/10.21203/rs.3.rs-354878/v1>`__. All measures used in the structure comparison tool are described in the methods and in "Extended data table 1".

.. _NGL: http://nglviewer.org
.. _OPM: https://opm.phar.umich.edu
	
Structure similarity trees
--------------------------

The Structure similarity trees is a tool that compares the overall conformation of a selected set of GPCR structures and generates a tree based on their shared conformational similarity.

Under the hood, this tool uses calculated distances from all Cα atoms to all other Cα atoms for all residues in the seven transmembrane helices. When a set of structures are being compared, first the average distance is calculated for each Cα atom pair and subsequently, this set of distances is filtered for all residues that are shared by at least 90% of all the structures. After this, for every structure, all the Cα distance pairs are normalized using the average distance for that specific Cα distance pair. After this, the similarity from each structure to each other structure is calculated using the summed absolute differences between all Cα distance pairs for those two structures. Finally, this sum of differences is normalized by the square of the distances divided by the square of the number of shared residues used in the comparison. Finally, the resulting all-against-all distance matrix is hierarchically clustered using average linkage clustering and a Newick tree is created from the results. The tree is subsequently enriched with additional data about each structure and the receptor. 

The online tool, the process is straightforward: after opening up the page click on the "Select Structures" button and select the structures to be compared in the selection panel that opened up (either by clicking on the row of a structure or by ticking the checkbox leftmost of the row). After closing the selection window, click on "Go" and the tree will be calculated. Using the dropdown menus, the tree can subsequently be manipulated by changing the tree type, the way the receptor/structure names are displayed and you can change the markers that are shown on the inside and outside of the structure names (leaves). Note that the internal nodes are colored with a white-to-black gradient (low-to-high) indicating the `Silhoutte index`_ , which is a measure of the separation of structures in this node to structures present in the nearest neighboring node. The quantitative value of this index is visible in a tooltip when hovering over the node.

In the top-right corner of the tree panel, three buttons can be found that allow to zoom in and out and recenter tree again. One level higher, in the top-right corner of the clustering panel, there are two icons, one for downloading the tree as a Figure, Newick tree, or the raw distance matrix, and one for making the panel full screen.

Finally, the tree is also interactive and can be used to make selections. When clicking on a node in the tree, the user gets the option to add the structures under that node to "selection set 1" or "selection set 2". Based on this selection, the user can directly start a structural analysis using the structure comparison tool to investigate the similarities and differences for the selected structures.

.. _Silhoutte index: http://dx.doi.org/10.1016/0377-0427(87)90125-7


Structure superposition
-----------------------

The superposition tool allows users to select two or more GPCR structures (or models) and superpose them based on a
user-specified segment selection. Using the tool is a two-step process.

1.  Select the structures to superpose. This can be done using the "structure browser" or by uploading the 
	PDB files. For the latter, only one reference structure can be uploaded, but multiple structures to be superposed on
	the reference can be uploaded. To select multiple structures for upload, hold down the Control key (or Command on Mac)
	while selecting.
2.  After structures have been uploaded or selected, the user is presented with a sequence segment selection page. The user 
	can select one or more sequence segments, and/or expand each segment to select the residues within it individually.
	Residues selected individually are grouped into a custom sequence segment.


Generic residue numbering (PDB)
-------------------------------

The PDB file residue numbering tool adds generic residue numbers from GPCRdb to any GPCR structure or model. This can
be useful when comparing structures visually.

A user simply uploads her structure and downloads a modified version of that structure, where b factors of certain
atoms have been replaced with generic numbers. Note that CA atoms will be assigned a number in GPCRdb notation, and N
atoms will be annotated with Ballesteros-Weinstein scheme.

On the structure download page, users can download scripts to visualize the generic numbers in `PyMOL`_ and `Maestro`_.

.. _PyMOL: https://pymol.org
.. _Maestro: https://www.schrodinger.com/Maestro
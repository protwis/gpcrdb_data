Sales and prescription (NHS)
============================

NHS sales 
---------

Every month, the National Health Service (NHS) in the UK publishes anonymised data about the drugs prescribed by general practitioners. NHS data were retrieved from openprescribing.net (DataLab-EBM, 2017, https://openprescribing.net/) (08/2017) for the list of drugs targeting GPCRs and mapped back to their reported target of therapeutic action. From the 475 queried FDA-approved drugs, data were available for 279 drugs targeting 92 distinct GPCRs (not all FDA-approved drugs are prescribed in the UK due to alternative treatments). 
The actual cost is the estimated cost to the NHS, which is usually lower than Net Ingredient Cost (“the basic price of a drug, i.e. the price listed in the Drug Tariff or price lists”). Openprescribing.net provides the actual cost by subtracting the average percentage discount per item received by pharmacists based on the previous month from the Net Ingredient Cost, but adding in the value of a container allowance for each prescription item (DataLab-EBM, 2017). 
Indications were grouped according to the British National Formulary (BNF), which is a reference book containing the standard list of medicines prescribed in the UK. Individual drugs can be selected (double click on colored bar chart) in the section page).

Drugs with NHS information can be filtered via the drug browser (column on the far right, NHS=yes).

Sales and variation information per drug is presented within the *Estimated economic burden* page. Here, sales and prescription averages are presented along with aggrgated counts of putative and known functional site variants of all receptors targeted by the drug.

Estimated economic burden
-------------------------

The economic burden estimate was calculated using the following formula:

*estimated economic burden per drug (£)* = *average NHS cost per drug per year (£)* **x** *%individuals with a  MV in a functional site of the respective drug targets*

where:
  * The average NHS cost is the average yearly cost over a 4-year period (2013-2016) per GPCR targeting drug that is listed (n=279). 2012 and 2017 have partial sales data and were not considered. 
  * % Individuals is the percentage of affected individuals with a missense variant in a functional site of the respective drug target(s) (n=2,504 individuals from 1,000 Genomes Project genotype data as a representative for the UK population; this data includes non-Caucasian populations as well) (Table S9). 
  * The % of affected individuals was calculated using four different criteria by considering individuals who have a variation in (i) known functional sites in both alleles (homozygous), which is the most conservative, (ii) known functional sites in at least one allele (i.e. homozygous and heterozygous), (iii) known or putative functional sites in both alleles (homozygous), and (iv) known or putative functional sites in at least one allele (i.e. homozygous and heterozygous), which is the least conservative.
  * Known functional sites include ligand binding, effector binding, PTM site, sodium binding site and micro-switches. Putative functional site include those predicted to be deleterious based on SIFT or PolyPhen (see above). 

More specifically, for each drug we collected the respective targets and computed economic burden using the following four criteria above: considering (i) % individuals with homozygous alleles in known functional sites, (ii) % individuals with at least one variant allele in a known functional site, (iii) % individuals with homozygous alleles in known or putative functional sites and (iv) % individuals with at least one variant allele in a known or putative functional sites. 

For these estimates, we have incorporated the following considerations (below). The economic burden estimates will vary if one scales/factors these variables differently:
	1. We have considered that each prescription (NHS data) is made for a unique individual, due to patient anonymity. Furthermore, information about the dose per prescription, and how this has been altered based on patient response is not explicitly modelled.
	2. The effect of known and putative site polymorphisms as well as homozygous/heterozygous conditions are all treated the same way. One could also obtain estimates by weighing these variables differently on a case-by-case basis for each receptor/drug.
	3. The focus has been prescription only from GPs. There might be significant additions to the economic burden if one also considers hospital prescriptions. 
	4. We used the data from 1000 Genomes Project as representative of the UK population, which may vary depending on the receptor.
	5. We have not explicitly modeled the age, gender, nature of illness (chronic v/s short-term) and mutations in non-coding regions, which may affect expression level.




Hauser, A. S., Chavali, S., Masuho, I., Jahn, L. J., Martemyanov, K., Gloriam, D. E., Babu, M. M., "Pharmacogenomics of GPCR drug targets", **2017**, *Cell*

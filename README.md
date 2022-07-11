# Phosphorus-cycling-database (PCyCDB)
This is a curated phosphorus cycling database (PCyCDB) with 138 gene families and 10 metabolism processes. 
Homologous genes were added into the database to reduce the false positive rate. The criteria (i.e., identity, hit length) for filtering the alignment result generated by sequence similarity searching tools (e.g., BLAST, USEARCH, DIAMOND) were refined by identifying a known simulated gene dataset and mock bacteria community to obtain the best accuracy and further reduction of false positives and false negatives. The accuracy, PPV, sensitivity, specificity and NPV were 99.76%, 95.70%, 99.94%, 99.74% and 99.99%, respectively, at the 70% identity and 25 amino acid cutoffs. 
Importantly, the genes encoding the intracellular phosphorus metabolic processes are added into PCyCDB, which should help researchers broaden the insights into not only the geochemical P cycling but also the microbial P metabolisms.

If you feel this database and utilities are useful, please cite:
Zeng J, Tu Q, Yu X, et al. PCycDB: a comprehensive and accurate database for fast analysis of phosphorus cycling genes[J]. Microbiome, 2022, 10(1): 1-16.

User guide:
1. Assuming you had a sample named $Sample.fa, and obtained a blast table named Sample.P.blast using BLAST+ or DIAMOND or other alignment tools, you can filter the result using filter_Generate_ORF2gene.py. 

Command: python filter_Generate_ORF2gene.py -s $identity -cov $alignment-coverage -hit $hitlength -b $Sample.P.blast

Recommended filtering threthold: it is acceptable to use 30% identity and 25 amino acids cutoffs to investigate more potential PCGs from metagenome sequencing data, because all known PCGs can be detected by PCycDB, while a little bit of predicted false-positive PCGs (1.04%) might also have the potential ability in mediating the P cycling. Also, one may use a stricter cutoff (i.e., 70% identity, 25 aa) to control the false positives (< 0.25%).

By doing this, you will obtain a ORF2gene file named $Sample.ORF2gene.txt, which descripts the P cycling gene for each ORF.

If you have a lot of sample for analysis, a bash for loop is recommend for quickly processing the data. For example:

for i in $Sample*.blast; do python filter_Generate_ORF2gene.py -s $identity -cov $alignment-coverage -hit $hitlength -b $i; done

2. Assuming you already have calculated the coverage (or TPM) using Bowtie2, CheckM, Salmon or other tools, and obtained a abuncance file named $Sample.quant for all ORFs, you can easily extracted the abuncance of PCGs using Coverage_get.py.

Command: python Coverage_get.py -i $Sample.ORF2gene.txt -t $Sample.quant -o $Sample.P.profile.txt

By doing this, you will obtain a abundance file for each PCG of the $Sample.

Extract_Seq.py was a useful python script for fast sequence extraction.
Command: python Extract_Seq.py -m $MAP -f $fasta -o $outputfile
Where $MAP contains the ORF id you wish to extract, $fasta is the sequence file from which for extraction, and $outputfile is the outputfile name. The file "pafAORF.list" is an example of $MAP. The file "pafAORF.nuc.fa" is the sequence of pafA gene analyzed in this paper.
Please note that this script uses {dictionary} function to fast extract the targeted sequence, it will preload all the sequence from $fasta into your system memory. 

3. Finally, you can merged all the $Sample.P.profile.txt into one matrix table using merge_metaphlan_tables.py provided by MetaPhlan. 

Reference

Integrating taxonomic, functional, and strain-level profiling of diverse microbial communities with bioBakery 3 Francesco Beghini, Lauren J McIver, Aitor Blanco-Míguez, Leonard Dubois, Francesco Asnicar, Sagun Maharjan, Ana Mailyan, Paolo Manghi, Matthias Scholz, Andrew Maltez Thomas, Mireia Valles-Colomer, George Weingart, Yancong Zhang, Moreno Zolfo, Curtis Huttenhower, Eric A Franzosa, Nicola Segata. eLife (2021)




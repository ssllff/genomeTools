#This script is to run multi-seq fasta blast against a database
#To use blast, first to download and install the NCBI blast+ standalone
#Check the command options at https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.options_common_to_all_blast
#Then build the blast databse
#For example, here is the command to build a nucleotide database
makeblastdb -in GCA_016097815.1_HAU_Weining_v1.0_genomic.fna  -dbtype nucl -out GCA_016097815.1_HAU_Weining_v1.0_genomic -title GCA_016097815.1_HAU_Weining_v1.0_genomic
#For compressed file
gunzip -c GCA_016097815.1_HAU_Weining_v1.0_genomic.fna.gz | makeblastdb -in - dbtype nucl <other options>
#Run blastn using default parameters, except using cutoff evalue is set as 10 and return results as a customized table summary (format 6)
blastn -db GCA_016097815.1_HAU_Weining_v1.0_genomic  -query SSRprimers.fas -evalue 10 -out blast.out -outfmt "6 qseqid sseqid pident length qstart qend sstart send evalue bitscore" 
#For short sequences use "-task blastn-short"
blastn -db GCA_016097815.1_HAU_Weining_v1.0_genomic  -query SSRprimers.fas -evalue 10 -out blast.out -outfmt "6 qseqid sseqid pident length qstart qend sstart send evalue bitscore" -task blastn-short

# Snakemake-workflow-dna-seq-short-read-blend-map
A Snakemake workflow (in progress) for mapping DNA PacBio sequencing data with BLEND.


This repository contains a Snakemake workflow designed to facilitate the analysis of NCBI single-ended SRA files using BLEND. The workflow is divided into three distinct Snakemake files, each handling specific tasks in the analysis pipeline.

Workflow Overview
##1. Snakemake File 1: Download and Initial Processing
+Downloads single-ended SRA files from NCBI using accessions specified in an accessions.txt file.
+Converts SRA files to FASTQ format.
+Performs quality control using FastQC and MultiQC.
##2. Snakemake File 2: Trimming and Additional QC
+Trims the FASTQ files to enhance data quality.
+Performs FastQC and MultiQC on the trimmed files for post-trimming quality assessment.
##3. Snakemake File 3: Blend Indexing and Mapping
+Indexes the reference genome for BLEND analysis.
+Maps the preprocessed reads to the indexed reference genome using BLEND.
+Converts SAM files to BAM format.
+Mapping Statistics Extraction
+Utilizes Samtools to extract mapping statistics, including overall statistics (samtools stats) and flag statistics (samtools flagstat).

##Usage
Prerequisites
Before running the workflow, ensure you have the necessary tools installed, such as fastqc, sra-tools, trimmomatic, samtools, and BLEND.

Running the Workflow
Clone this repository:

bash
Copy code
git clone https://github.com/fulbelin/Snakemake-workflow-dna-seq-short-read-blend-map.git
cd your-repo
Prepare an accessions.txt file and trimmed_acessions txt file with the desired SRA accessions for download and trimming.

Execute the Snakemake files sequentially:

bash
Copy code
snakemake --snakefile Snakefile1 --cores 1 --latency-wait 30
snakemake --snakefile Snakefile2 --cores 1 --latency-wait 30
snakemake --snakefile Snakefile3 --cores 1 --latency-wait 30

Notes
Each Snakemake file is modular, allowing for independent execution or integration into other workflows.
Adjust the parameters in the Snakemake files according to your specific needs.
Feel free to customize and extend this workflow to suit your requirements. For detailed information on each step and the parameters used, refer to the respective Snakemake files and associated configuration files.

If you encounter issues or have suggestions for improvements, please open an issue in the repository. Happy analyzing!









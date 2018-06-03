# runITASSER
Wrapper to Run ITASSER on a local computer to predict structures of a protein from its sequence in a FASTA file.

Install I-TASSER (https://zhanglab.ccmb.med.umich.edu/I-TASSER/download/) by following the instructions contained in the webpage. Update the variable "bdir" in the script to point to the i-tasser installation directory.

Usage: runITASSER.py <input file path> <name of sequence in the file>
  
 input file path: the path to fasta file containing the sequence
 
 name of sequence in the file: the header of the sequence for which we need to predict structures

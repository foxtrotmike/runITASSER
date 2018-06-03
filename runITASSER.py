#!/mirror/anaconda2/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:02:06 2016
Script to run I-TASSER on local computer
@author: afsar
"""
import os
import sys
import string
import random
from Bio import SeqIO
#print sys.argv    
if len(sys.argv)!=3:
    raise Exception("Usage: runITASSER.py <input file path> <name of sequence in the file>")
ifile = sys.argv[1]
sname = sys.argv[2].lower()

def randStr(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# read input file and identify the sequence to be read-in
for record in SeqIO.parse(ifile, "fasta"):
    if record.id.lower() == sname.lower():
        break
else:
    raise Exception("Could Not find "+sname+" in "+ifile )
    
bdir = "/mirror/pairpred_tools/i-tasser/"

sname += '_'+randStr()
ddir = os.path.join(bdir,"inputs/"+sname)
print "Creating Directory",ddir
os.mkdir(ddir)
print "Created Output Directory",ddir
record.id = sname
ifpath = os.path.join(ddir,'seq.fasta')
print "Writing Sequence File",ifpath
with open(ifpath,'w') as fh:
    SeqIO.write(record, fh, "fasta")
print "Wrote:",ifpath   
logfile = os.path.join(ddir,"log_run.txt")
pkgpath = os.path.join(bdir,"I-TASSER5.0")
scrpath = os.path.join(pkgpath,"I-TASSERmod/runI-TASSER.pl")
libpath = os.path.join(bdir,"ITLIB")
cmd = scrpath+" -pkgdir "+pkgpath+" -libdir "+libpath+" -seqname "+sname+" -datadir "+ddir+" > "+logfile +" &"
print "Executing Command", cmd
os.system(cmd)
print "Running, Results will be in", ddir
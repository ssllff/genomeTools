from __future__ import with_statement
from sys import argv, stderr, stdin, exit, stdout
from getopt import getopt, GetoptError
from Bio import SeqIO
import Bio
from Bio.SeqRecord import SeqRecord
from collections import defaultdict


def renameFasta(inputFile, outputFile, idFile):
    '''
    This function translate each sequence in cdsFile to protein
    Write into protFile
    '''
    idDict=defaultdict(str)
    chrName=[]
    with open(idFile, "r") as fp:
        for line in fp:
            [new, old] = line.strip("\n").split("\t")
            idDict[old]=new
            chrName.append(old)
    
    seq_rec = list(SeqIO.parse(inputFile, 'fasta'))
    my_rec=[]
    for chr in chrName:
        for nuc_rec in seq_rec:
            if nuc_rec.id == chr:
                nuc_rec.id=idDict[nuc_rec.id]
                nuc_rec.description=nuc_rec.id
                my_rec.append(nuc_rec)
    SeqIO.write(my_rec, outputFile, "fasta")
    print "Done"
    
if __name__ == "__main__":
    try:
        opts, args = getopt(argv[1:], "hd",["help", "debug"])
    except GetoptError, err:
        print str(err)
        print >> stderr, __doc__
        exit(2) 

    for o, a in opts:
        if o in ("-h", "--help"):
            print >> stderr, __doc__
            exit()
        elif o in ("-d", "--debug"):
            debug_flag = True
        else:
            assert False, "unhandled option"

    if len(args) > 3:
        print >> stderr, __doc__
        exit(3)

    renameFasta(args[0], args[1], args[2])

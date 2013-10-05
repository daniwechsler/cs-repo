#
# CS Problem 9
# Author: Daniel Wechsler
#

#
# Compares two sequences given as strings.
#
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from Bio import ExPASy, SeqIO, Phylo


#
# Given two sequences seqA and seqB the function creates
# a dotplot (using the given region size) and stores the
# plot as an image (directory plots/)
#
def dotPlotSequences (seqA, seqB, regionSize, titleA = "", titleB = "") :
    
    lenA = len(seqA)
    lenB = len(seqB)
    
    y = []          
    x = []
    for n in range(0, lenA-regionSize+2) :
        regionAn = seqA[n:n+regionSize]

        for k in range (0, lenB-regionSize+2) :
            regionBk = seqB[k:k+regionSize]
        
            if str(regionAn) == str(regionBk) :
                y.append(n)
                x.append(k)
        

    # Create plot and write it to file                  
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.plot(x, y, '.')
    ax.set_title("Pairwise dot plot (" + str(titleA) + "/" + str(titleB) + ") - Region size: " + str(regionSize))
    plt.xlabel(titleA)
    plt.ylabel(titleB)
    plt.savefig("plots/" + str(regionSize) + "-"  + titleA + "-" + titleB + "-.png")   




def drawNewickTree () :
    tree = Phylo.read("tree.txt", "newick")
    tree.rooted = True
    Phylo.draw(tree)
    




"""
Gene: FOXP2
-----------
FOXP2_MOUSE		Mus musculus (Mouse)
FOXP2_GORGO             Gorilla gorilla gorilla (Lowland gorilla)
FOXP2_PANTR		Pan troglodytes (Chimpanzee)
FOXP2_RAT		Rattus norvegicus (Rat)
FOXP2_HUMAN		Homo sapiens (Human)
"""

regionSize   = 100
sequenceFils = [
    "FOXP2_MOUSE", 
    "FOXP2_GORGO",
    "FOXP2_PANTR",
    "FOXP2_RAT",
    "FOXP2_HUMAN"]
sequences = []


# Read all sequence files defined in the list (directory genbank-files/)
for file in sequenceFils :
    handle = open("genbank-files/" + file + ".genbank", "rU")
    for record in SeqIO.parse(handle, "genbank") :
        sequences.append(record.seq)
       
    handle.close()


# Compute dot plot for each pair (directory plots/)
dotPlotSequences (sequences[0], sequences[1], regionSize, "Mouse", "Gorilla")
dotPlotSequences (sequences[0], sequences[2], regionSize, "Mouse", "Chimpanzee")
dotPlotSequences (sequences[0], sequences[3], regionSize, "Mouse", "Rat")
dotPlotSequences (sequences[0], sequences[4], regionSize, "Mouse", "Human")
dotPlotSequences (sequences[1], sequences[2], regionSize, "Gorilla", "Chimpanzee")
dotPlotSequences (sequences[1], sequences[3], regionSize, "Gorilla", "Rat")
dotPlotSequences (sequences[1], sequences[4], regionSize, "Gorilla", "Human")
dotPlotSequences (sequences[2], sequences[3], regionSize, "Chimpanzee", "Rat")
dotPlotSequences (sequences[2], sequences[4], regionSize, "Chimpanzee", "Human")
dotPlotSequences (sequences[3], sequences[4], regionSize, "Rat", "Human")

# Results:
#
# The less perforated the diagonal is the more similare the compared amino-acid sequences are.
# (And the closer the species are related).
# ,
# 



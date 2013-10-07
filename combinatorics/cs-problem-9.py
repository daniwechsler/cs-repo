#
# CS Problem 9
# Author: Daniel Wechsler
#

import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from Bio import ExPASy, SeqIO, Phylo


#
# Given two sequences seqA and seqB the function creates
# a dot plot (using the given region size) and stores the
# plot as an image (directory plots/)
#
def dotPlotSequences (seqA, seqB, regionSize, titleA = "", titleB = "", pdf = None) :
    
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

    # If given, write plot to the pdf file
    if pdf != None:
         plt.savefig(pdf, format='pdf')    


#
# Draws Newick tree from file with given name.
#
def drawNewickTree (fileName) :
    tree = Phylo.read(fileName, "newick")
    tree.rooted = True
    Phylo.draw(tree)
    



#
# Gene: FOXP2
# -----------
#
# Id                    Species
# ==============================================================
# FOXP2_MOUSE		Mus musculus (Mouse)
# FOXP2_GORGO           Gorilla gorilla gorilla (Lowland gorilla)
# FOXP2_PANTR		Pan troglodytes (Chimpanzee)
# FOXP2_RAT		Rattus norvegicus (Rat)
# FOXP2_HUMAN		Homo sapiens (Human)
#

regionSize   = 50
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


# Create a pdf showing all plots
pdf = PdfPages("plots/dot_plots-" + str(regionSize) + ".pdf")

# Compute dot plot for each pair (directory plots/)
dotPlotSequences (sequences[0], sequences[1], regionSize, "Mouse", "Gorilla", pdf)
dotPlotSequences (sequences[0], sequences[2], regionSize, "Mouse", "Chimpanzee", pdf)
dotPlotSequences (sequences[0], sequences[3], regionSize, "Mouse", "Rat", pdf)
dotPlotSequences (sequences[0], sequences[4], regionSize, "Mouse", "Human", pdf)
dotPlotSequences (sequences[1], sequences[2], regionSize, "Gorilla", "Chimpanzee", pdf)
dotPlotSequences (sequences[1], sequences[3], regionSize, "Gorilla", "Rat", pdf)
dotPlotSequences (sequences[1], sequences[4], regionSize, "Gorilla", "Human", pdf)
dotPlotSequences (sequences[2], sequences[3], regionSize, "Chimpanzee", "Rat", pdf)
dotPlotSequences (sequences[2], sequences[4], regionSize, "Chimpanzee", "Human", pdf)
dotPlotSequences (sequences[3], sequences[4], regionSize, "Rat", "Human", pdf)

pdf.close()

# Results:
#
# The less perforated the diagonal is the more similar the compared amino-acid sequences are
# (And the closer the species are related).
# Evaluating the dot plots gives to following:
#
# Region Size: 50 Characters
#
# Species A     Species B       Similarity* (%)
# ============================================
# Mouse         Gorilla         89     
# Mouse         Chimpanzee      88         
# Mouse         Rat             81
# Mouse         Human           80
# Gorilla       Chimpanzee      99
# Gorilla       Rat             84
# Gorilla       Human           90
# Chimpanzee    Rat             84
# Chimpanzee    Human           90
# Rat           Human           78
#
# * Similarity is computed by measuring gap size on plot (manually).
# * Common gaps between different species are indicators that they are descendent 
#   of each other or have a common ancestor.
#
# I tried to build a tree diagram (Newick) from what I found in the dot plots:
# 

drawNewickTree("tree.txt")










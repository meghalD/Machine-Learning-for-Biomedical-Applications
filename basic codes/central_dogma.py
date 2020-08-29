from Bio.Seq import Seq #import biopython Seq library
print("visualisation of sequences in Central Dogma of Life!")
dna = input("enter dna sequence : ") #input data
dna_seq = Seq(dna)
#transcribe dna to rna
rna = dna_seq.transcribe()
print("mrna formed is : ",rna)
#translate rna to protein
protein = rna.translate()
print("protein formed is: ",protein)
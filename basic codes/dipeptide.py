from Bio import SeqIO
amino_acid=['G','A','V','L','I','P','F','Y','W','S','T','C','M','N','Q','K','R','H','D','E'] #list of all amino acids
didpeptide=['']*400 #list to store all dipeptides
pept_comp={}

n=len(amino_acid)
k=0
#formation of all dipeptides
for i in range(n):
    for j in range(n):
        didpeptide[k]=amino_acid[i]+amino_acid[j]
        k=k+1

#print(amino_acid)
#print(didpeptide)
#initialising dipeptide composition of each dipeptide = 0
for j in range(len(didpeptide)):
    pept_comp[didpeptide[j]]=0
#print(pept_comp)
filename=input("enter file name along with path : ")
fileD=open(filename,"r")
while True:

    data=fileD.readline() #read each sequence for composition calculation

    if data=='':
        break
    for i in range(len(data)):
        for j in range(len(didpeptide)):
                count=data.count(didpeptide[j])
                pept_comp[didpeptide[j]]=(count/len(data))*100



print("didpeptide composition is as : \n ",pept_comp)


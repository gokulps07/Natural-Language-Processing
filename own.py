# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 21:35:59 2020

@author: PSG
"""
import pandas as  pa
import numpy as np
import matplotlib.pyplot as mpl

data=pa.read_csv('NLP.tsv',delimiter='\t',quoting=3)
x=data.iloc[:,0].values
y=data.iloc[:,1].values
import re
word=input()
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
cor=[]

rev1=re.sub('[^A-Za-z]', ' ',word)
rev1=rev1.lower()
rev1=rev1.split()
ps=PorterStemmer()
rev1=[ps.stem(i) for i in rev1 if i not in set(stopwords.words('english'))]
#rev=' '.join(rev)

print(rev1)
bow=np.zeros((1000, len(rev1)))
for i in range  (0,1000):
    rev=re.sub('[^A-Za-z]', ' ',data['Review'][i])
    rev=rev.lower()
    rev=rev.split()
    ps=PorterStemmer()
    
    rev=[ps.stem(i) for i in rev if i not in set(stopwords.words('english'))]
    rev=' '.join(rev)
    cor.append(rev)
    
for i in range (len(cor)):
    for j in range (len(rev1)):
        if rev1[j] in cor[i]:
            bow[i][j]=1
            
prs=np.zeros(((len(rev1))))
pr=np.zeros(((len(rev1))))
c=0
for i in range (len(prs)):
    for j in range(len(y)):
        if(bow[j][i]==1):
            pr[i]=pr[i]+1
        if(y[j]==1 ):
            if(i==0):
                c=c+1
            if(bow[j][i]==1):
                prs[i]+=1
    if(pr[i]==0):
            pr[i]=100
        
    if(prs[i]==0):
            prs[i]=100  
if(c==0):
    c=2
prs1=np.zeros(((len(rev1))))
pr1=np.zeros(((len(rev1))))    

pr1=(1000-prs)/1000
s=c/1000    
prs/=500        
pr/=1000
r = np.prod(s)
r1 = np.prod(prs)
r2 = np.prod(pr)
Output=(r1*r)/r2
for i in range (len(prs1)):
    for j in range(len(y)):
        if(bow[j][i]==1 and y[j]==0):
            prs1[i]+=1
    if(prs1[i]==0):
            prs1[i]=100 
prs1/=500            
r = np.prod(s)
r1 = np.prod(prs1)
r2 = np.prod(pr1)
Output1=(r1*r)/r2
we=Output
#Regularization Of Output
Output=(Output/(Output+Output1))
Output1=(Output1/(we+Output1))


if(Output>0.5):
    print("Postive Result")
else:
    print("Negative Result")       


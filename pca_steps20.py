#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:13:33 2021

@author: gorangiudetti
edited by sraddhaagrawal
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris = load_iris()
colors = ["blue", "red", "green"]

feat = ["r2",	"r3",	"a3",	"r4",	"a4",	"d4",	"r5",	"a5",	"d5",	"r6",	"a6",	"d6",	"r7",	"a7",	"d7",	"r8",	"a8",	"d8",	"r9",	"a9",	"d9",	"r10",	"a10",	"d10",	"r11",	"a11",	"d11",	"r12",	"a12",	"d12",	"r13",	"a13",	"d13",	"r14",	"a14",	"d14",	"r15",	"a15",	"d15",	"r16",	"a16",	"d16",	"r17",	"a17",	"d17",	"r18",	"a18",	"d18",	"r19",	"a19",	"d19",	"r20",	"a20",	"d20",	"r21",	"a21",	"d21",	"r22",	"a22",	"d22",	"r23",	"a23",	"d23",	"r24",	"a24",	"d24",	"r25",	"a25",	"d25",	"r26",	"a26",	"d26",	"r27",	"a27",	"d27",	"r28",	"a28",	"d28",	"r29",	"a29",	"d29",	"r30",	"a30",	"d30",	"r31",	"a31",	"d31",	"r32",	"a32",	"d32",	"r33",	"a33",	"d33",	"r34",	"a34",	"d34",	"r35",	"a35",	"d35",	"r36",	"a36",	"d36",	"r37",	"a37",	"d37",	"r38",	"a38",	"d38",	"r39",	"a39",	"d39",	"r40",	"a40",	"d40",	"r41",	"a41",	"d41",	"r42",	"a42",	"d42",	"r43",	"a43",	"d43",	"r44",	"a44",	"d44",	"r45",	"a45",	"d45",	"r46",	"a46",	"d46",	"r47",	"a47",	"d47",	"r48",	"a48",	"d48",	"r49",	"a49",	"d49",]

NMI = []
for i in feat:
    o=open("MI_not_rounded/MI_%s.txt" % i, "r")
    o1 = o.readlines()
    o2 = o1[3].strip().split()
    NMI.append(o2[6])
    o.close()
    
# print(feat)
# print(NMI)

zipped_lists = zip(NMI,feat)
sorted_pairs = sorted(zipped_lists, reverse=True)

tuples = zip(*sorted_pairs)
SNMI, Sfeat = [ list(tuple) for tuple in  tuples]

#print(SNMI)
#print(Sfeat)

tmp=(np.array(SNMI[0:10]))
tmp1= tmp.astype(float)
tmp_value=np.round(tmp1, decimals=4)

#print(tmp_value)

plt.rcdefaults()
fig, ax = plt.subplots()


df = pd.DataFrame ({
       'coord' : Sfeat[0:10],
       'value' : tmp_value
})       
#error = np.random.rand(len(coord))
df = df.sort_values(by=['value'])

print (df)

# plt.barh(y=df.coord, width=df.value);
# plt.xlabel('Mutual Information')
# plt.xlim([0.86,0.905])
# #ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
# plt.savefig('MI_not_rounded_step20.png',dpi=100)

df = pd.DataFrame(np.zeros((1092,len(SNMI[0:10]))), columns=Sfeat[0:10])
#print(df)

for x in Sfeat[0:10]:
    f = open("CLEAN/all_%s_internal_clean1.txt" % x,"r")
    f1 = f.readlines()
    F = []
    #for z in range(0,len(f1)):
    for z in range(0,len(f1)):
        f2 = f1[z].strip().split()
        F.append(f2[1])
    df[x] = F
    df[x] = df[x].astype(float)
    pd.options.display.float_format = "{:,.2f}".format
    
    f.close()


corrMatrix = df.corr()

#corrMatrix=corrMatrix1(20,20)

#print (df)
#print (corrMatrix)

# sns.heatmap(corrMatrix, annot = True, fmt=".2f", annot_kws={"size":6})
# sns.color_palette("flare", as_cmap=True)

# plt.savefig('corr_not_rounded_step20.png',dpi=100)

u, s, v = np.linalg.svd(corrMatrix, full_matrices=True)

#svd_scores = np.dot(corrMatrix, v.T[:, :2])

# print ('*'*10 , "v matrix" , '*'*10)
# print (v)
# print ('*'*10 , "v matrix transpose" , '*'*10)
# print (v.T)
# print ('*'*10 , "v matrix transpose : 2" , '*'*10)
# print (v.T[:,:2])

# biplot(svd_scores, v.T, iris["feature_names"])
# plt.legend()
# plt.savefig("biplot_svd.png")

#print(svd_scores)

#print(u)
print(s)
#print(v)

var_explained = np.round(s**2/np.sum(s**2), decimals=3)

#print (var_explained)
 
sns.barplot(x=list(range(1,len(var_explained)+1)),
             y=var_explained, color="limegreen")
plt.xlabel('SVs', fontsize=16)
plt.ylabel('Percent Variance Explained', fontsize=16)
plt.savefig('svd_scree_plot_20.png',dpi=100)


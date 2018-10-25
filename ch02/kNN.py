
# coding: utf-8

# In[40]:


import numpy as np
import pandas as pd
import operator


# In[41]:


def loadData():
    df=pd.read_table("./ds/datingTestSet.txt",header=None,delim_whitespace=True)
    ds=df[[0,1,2]].values
    labels=df[3].replace("didntLike",0).replace("smallDoses",1).replace("largeDoses",2).values
    return ds,labels


# In[43]:


def kNN(inX,ds,labels,k):
    rows=ds.shape[0]
    inXs=np.tile(inX,(rows,1))
    diff=inXs-ds
    sqDiff=diff**2
    sqDistances=sqDiff.sum(axis=1)
    distances=sqDistances**0.5
    #排序
    sortedDistanceIndicies=distances.argsort()
    classCount={}
    for i in range(k):
        voteILabel=labels[sortedDistanceIndicies[i]]
        classCount[voteILabel]=classCount.get(voteILabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]   


# In[44]:


# newVal=(oldVal-minVal)/(maxVal-minVal)
def autoNorm(dataSet):
    #获取列的最小值
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    rows=dataSet.shape[0]
    temp=dataSet-np.tile(minVals,(rows,1))
    normDs=temp/np.tile(ranges,(rows,1))
    return normDs,ranges,minVals



# In[50]:


ds,labels=loadData()
newDs,ranges,minVals=autoNorm(ds)
kNN(newDs[2],newDs,labels,3)


# In[75]:


def datingClassTest(ratio,k):
    hoRatio=ratio
    ds,labels=loadData()
    newDs,ranges,minVals=autoNorm(ds)
    rows=ds.shape[0]
    num=int(rows*hoRatio)
    errors=0
    for i in range(num):
        r=kNN(newDs[i,:],newDs[num:rows,:],labels[num:rows],k)
        #print("the classifier came back with :%d,the real answer is :%d"%(r,labels[i]))
        if(r!=labels[i]):
            errors+=1
    print("the total error rate is %f,k=%d,ratio=%f" %(errors/num,k,ratio))        


# In[80]:


datingClassTest(0.1,4)
print('==========================================')
for i in range(10):
    for j in range(10):
        datingClassTest(0.1+0.01*j,i+1)


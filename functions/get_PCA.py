#----------------------------------------------------------------------------------------
# GET PCA
#----------------------------------------------------------------------------------------
import numpy as np

def Get_PCA(PCA): # to get it once only  
    nrns = len(PCA.keys())
    orderneurons = np.sort(list(PCA.keys()))
    #------------------------------------
    #initialize params
    PCA1=[]
    PCA2=[]
    PCA3=[]
    color=[]
    #------------------------------------
    #iteration for PCA and cluster colors
    i=0	
    for neuron in  orderneurons[:]:
        PCAdata = PCA[neuron].PCA_wave

        PCA1 = np.append(PCA1,PCAdata[6])
        PCA2 = np.append(PCA2,PCAdata[5])
        color = np.append(color,PCA[neuron].clus_label)
        i+=1
    cl1 = np.where(color==1)
    cl2 = np.where(color==0)
    return [PCA1,PCA2],[cl1,cl2]

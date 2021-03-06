#!/usr/bin/env python
#coding=utf-8

# FUNCTIONS SURPRISE FOR single neuron
# Functions in this file are:
#		- display_surprise(Surprise,binsizes, n ,  fig, inner_grid, wb, nth):
#		- display_surprisePW(Surprise, n ,  fig, inner_grid, wb, nth):


from matplotlib.pyplot import*
from numpy import*
import numpy as np

#----------------------------------------------------------------------------------------
# DISPLAY SURPRISE
#----------------------------------------------------------------------------------------
def display_surprise(Surprise,binsizes, n ,  fig, inner_grid, wb, Thresh):

    Surp = Surprise.Data
    
    #fig = figure(figsize=(12,40))
    #fig.subplots_adjust( hspace=0.4,wspace=0.15)

    bincount=0
    for binsize in binsizes: #arange(20)+1:

        bincount+=1
        for d in [0,1]:
            ax= Subplot(fig, inner_grid[(bincount-1)*4+d*2])
            #ax = fig.add_subplot(4*len(binsizes),4,(bincount-1)*4+d*2+1)
            if bincount== 1  and d==0:
                ax.text(25,1.3,'Caudal', size = 12, fontweight='bold')
            if bincount== 1  and d==1:
                ax.text(25,1.3,'Rostral', size = 12, fontweight='bold')
            if d==0:
                ax.set_ylabel('Binsize ' + str(binsize), size = 12)
            if bincount == 1:
                ax.set_title('Cumulative surprise')    
            if bincount == len(binsizes):
                ax.set_xlabel('Surprise value ')
                #' - Direction' + str(d) 
            #---------------------------------------------------------------------------------------------
            # Cumulative surprise
            for w in arange(25):
                sorted_data = np.sort(Surp[w][binsize][d][5:])
                cumulative = np.cumsum(sorted_data)
                yvals=np.arange(len(sorted_data))/float(len(sorted_data))
                ax.plot( sorted_data, 1-yvals )
            y = Thresh[binsize-1]
            
            ax.plot([y,y],[0,1],'-r', lw = 2 )
            ax.set_xlim([0,27])
            ax.set_ylim([0,1])
            #---------------------------------------------------------------------------------------------
            # Cumulative Blank Surprise
            sorted_datab = np.sort(Surp[wb][binsize][d])    
            yvalsb=np.arange(len(sorted_datab))/float(len(sorted_datab))
            ax.plot( sorted_datab, 1-yvalsb,'b',lw=4 )
            
            ax.set_yticks([0,0.5,1])
            ax.tick_params( labelsize=8)
            fig.add_subplot(ax)
            #---------------------------------------------------------------------------------------------
            # Surprise
#            ax = fig.add_subplot(4*len(binsizes),4,(bincount-1)*4+d*2+2)
            ax= Subplot(fig, inner_grid[(bincount-1)*4+d*2+1])
            if bincount == 1:
                ax.set_title('Surprise')
            if bincount == len(binsizes):
                ax.set_xlabel('Time (ms) ')
            #ax.set_title()
            for w in arange(25):
                ax.plot(Surp[w][binsize][d])
            # Blank    
            ax.plot(Surp[wb][binsize][d][0:55],'b',lw=5)
            ax.set_xlim([0,54])
            #---------------------------------------------------------------------------------------------
            # Threshold
            y=[]
            ystd=[]
            y = Thresh[binsize-1]
            
            ax.plot([0,54],[ y , y ],'-r', lw = 2 )

            #--------------------------------------------------------------------------------------------
            ax.set_yticks([0,10,20,30])
            ax.tick_params( labelsize=8)
            fig.add_subplot(ax)
    
    return

#----------------------------------------------------------------------------------------
# DISPLAY SURPRISE FOR PW
#----------------------------------------------------------------------------------------
def display_surprisePW(Surprise,Sig, n ,  fig, inner_grid, wb, Thresh):

    Surp = Surprise.Data
    PW = Sig.PW
   
    for d in [0,1]:
        #---------------------------------------------------------------------------------------------
        # Surprise
        ax= Subplot(fig, inner_grid[d+2])
        # Blank    
        for binsize in arange(20)+1:
            ax.plot(Surp[wb][binsize][d],'b',lw=2)
        for binsize in arange(20)+1:
            w = PW[d]
            ax.plot(Surp[w][binsize][d])
        
        ax.set_xlim([0,54])
                
        #---------------------------------------------------------------------------------------------
        # Threshold
        for binsize in [1,5,10,15]:
            y=[]
            ystd=[]
            y = Thresh[binsize]*0.5
            ax.plot([0,54],[ y , y ],'orange', lw = 0.1 )
            #ax.plot([0,54],[ y , y ],'-r', lw = 2 )

        #---------------------------------------------------------------------------------------------
        
        if d==0 :
            ax.set_title('PW Caudal', size =10, fontweight='bold')    
            ax.set_ylabel('Surprise', size=12)
        else:
            ax.set_title('PW Rostral',size =10, fontweight='bold')    
        ax.set_xlabel('Time (ms)')
        
        ax.tick_params( labelsize=8)
        ax.set_yticks([0,10,20,30])

        fig.add_subplot(ax)
        
    return

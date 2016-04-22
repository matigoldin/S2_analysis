# display_all_PSTHs_of_recording
# used previously than surprise, have to correct if wanting to use again

#----------------------------------------------------------------------------------------
# DISPLAY ALL PSTH
#----------------------------------------------------------------------------------------
def display_all_PSTHs_of_recording(expe,histdata, counts, pdf_files_directory, t_before, t_after,grupete,titles) :
    
    fig = plt.figure(figsize=(12,16.5))
    nrns = len(histdata.keys())
    if nrns <16: 
        layout = [5,3]
    else: layout = [nrns//3+(nrns%3!=0),3]
    outer_grid = gridspec.GridSpec(layout[0], layout[1], wspace=0.1, hspace=0.2)
    
    ii=0
    orderneurons = np.sort(list(histdata.keys()))
    for neuron in  orderneurons:
        clf()
        totalup = 0
        totaldown = 0
        for i in np.arange(25, dtype='int') :
            totalup+=counts[neuron][i][0]
            totaldown+=counts[neuron][i][1]
            
        inner_grid = gridspec.GridSpecFromSubplotSpec(5,5,subplot_spec=outer_grid[ii], wspace=0.1, hspace=0.1)
               
        numspikesP= totalup                  
        numspikesN= totaldown
        
        Sig = numpy.zeros(25, dtype=bool)
        PW = 20
        
        display_PSTH(expe,histdata[neuron], counts[neuron], t_before, t_after,fig,inner_grid,neuron,numspikesP,numspikesN,Sig,PW)                               
        
        if grupete ==1:
            fig.suptitle(titles + '_multiunits',fontsize=16)
        elif grupete ==3:
            fig.suptitle(titles + '_responsiveMULTIUNITS',fontsize=16)
        else:
            fig.suptitle(titles ,fontsize=16)
        
        ii+=1
    if grupete ==1:                  
        fig.savefig(pdf_files_directory + titles + '_hist_multi.pdf', format='pdf')
    elif grupete==3:
        fig.savefig(pdf_files_directory + titles + '_hist_respMULTI.pdf', format='pdf')
    else:        
        fig.savefig(pdf_files_directory + titles + '_hist.pdf', format='pdf')


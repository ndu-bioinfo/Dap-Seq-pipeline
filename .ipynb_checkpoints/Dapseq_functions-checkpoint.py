def Tandem_filter(fasta_file,k = 6,k_max = 3):

    # Import libs
    import itertools
    from Bio import SeqIO
    import matplotlib.pyplot as plt
    
    # k-mer based tandem filter 
    list_k_mer = [''.join(c) for c in itertools.product(['A','C','G','T'], repeat=k)]
    
    with open(fasta_file,'r') as handle:
        dict_fasta = SeqIO.to_dict(rec.upper() for rec in SeqIO.parse(handle,'fasta'))
    
    # Remove sequences that have tandem repeats
    Output_Seq = [] # Sequence that will be used for peak calling
    Clear_Seq = [] # Sequence that will be removed
    peak_loc = [] 
    kmer_list = []
    N_loc = []
    for seq in dict_fasta:
        kmer_count = [dict_fasta[seq].seq.count(kmer) for kmer in list_k_mer]
        top_kmer = list_k_mer[kmer_count.index(max(kmer_count))]
        peaks = [kmer.start() for kmer in re.finditer(top_kmer, str(dict_fasta[seq].seq))]
        Ns = [kmer.start() for kmer in re.finditer(str('N'), str(dict_fasta[seq].seq))]
        if len(peaks)>=k_max or len(Ns)>1:
            peak_loc.append(peaks)
            Clear_Seq.append(dict_fasta[seq])
            kmer_list.append(top_kmer)
            N_loc.append(Ns)
        else:
            Output_Seq.append(dict_fasta[seq])
            
    # Plot all removed sequences for quality control        
    f,ax = plt.subplots(int(len(Clear_Seq)/3)+1,3,figsize = (12,max(3,int(len(Clear_Seq)/10))))
    [axi.set_axis_off() for axi in ax.ravel()]
    ax = ax.ravel()
    plt.suptitle(fasta_file.split('/')[-1].split('.')[0])
    for ix,seq in enumerate(Clear_Seq):
        ax[ix].plot([0,len(seq)],[0,0],'lightblue')
        if len(N_loc[ix])>1:
            ax[ix].plot([N_loc[ix][0],N_loc[ix][-1]],[0,0],'grey')
        for x in peak_loc[ix]:
            ax[ix].plot([x,x+k],[0,0],'r')
            if k_max > 2:
                ax[ix].set_title(kmer_list[ix]+'='+str(len(peak_loc[ix])),fontsize = 10)   
    with open(fasta_file[:-5]+'filtered.fasta','w') as output_handle:
        SeqIO.write(Output_Seq, output_handle, "fasta")
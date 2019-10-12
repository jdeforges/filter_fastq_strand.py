	import pysam
    from Bio import SeqIO
    import sys
    
    #####################################################################################
    # 1/ function to extract read names from bam
    def getReadNames(filein):
            listID = []
            BAM = pysam.AlignmentFile(filein, "rb")
            for Read in BAM.fetch():
                    listID.append(Read.query_name)
            BAM.close()
            return listID
    
    #####################################################################################
    # 2/ function to extract reads from fastq files with ID matching those in listID
    def ExtractReads(filein, fileout, listID):
            record_dict = SeqIO.index(filein, "fastq")
            Out = open(fileout, 'w')
            for ID in set(listID):
                    Out.write(record_dict[ID].format('fastq'))
            Out.close()
    
    def main(sample):
            bamfile = "Mapping/" + "$SAMPLE" + "_" + "$INDEX" + "_strand.bam"
            listID = getReadNames(bamfile)
            R1 = "Fastq/" + "$SAMPLE" + "_L8_R1.fastq"
            R2 = "Fastq/" + "$SAMPLE" + "_L8_R2.fastq"
            R1out = "Filtered_fastq/" + "$SAMPLE" + "_" + "$INDEX" + "_L8_R1.fastq"
            R2out = "Filtered_fastq/" + "$SAMPLE" + "_" + "$INDEX" + "_L8_R2.fastq"
            ExtractReads(R1, R1out, listID)
            ExtractReads(R2, R2out, listID)
    
    sample = sys.argv[1]
    index = sys.argv[2]
    
    main(sample)
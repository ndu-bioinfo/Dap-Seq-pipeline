#!/usr/bin/env python
import argparse,os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--THREADS', type=str, default = '1', help = 'Number of threads')
    parser.add_argument('-i', '--inputfile', type=str)
    parser.add_argument('-o', '--outputfile', type=str)
    opts = parser.parse_args()

    THREADS = opts.THREADS
    input_file = opts.inputfile
    output_file = opts.outputfile
    
    cmd = '/usr/local/bin/samtools view -@ ' +THREADS+' -h -F 4 -q 30 -u -S '+input_file+' | samtools sort -@ '+THREADS+' - '+output_file
    
    os.system(cmd)
    #print(cmd)
        
if __name__ == "__main__":
    main()
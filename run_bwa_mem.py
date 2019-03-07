#!/usr/bin/env python
import argparse,os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--THREADS', type=str, default = '1', help = 'Number of threads')
    parser.add_argument('-k', '--Minimum_seed_length', type=str, default = '10', help = 'Matches shorter than INT will be missed. The alignment speed is usually insensitive to this value unless it significantly deviates 20.')
    parser.add_argument('-B', '--Mismatch_penalty', type=str, default = '4', help = 'The sequence error rate is approximately: {.75 * exp[-log(4) * B/A]}.')
    parser.add_argument('-O', '--Gap_open_penalty', type=str, default = '1')
    parser.add_argument('-v', '--verbose', type=str, default = '10', help = 'Control the verbose level of the output. This option has not been fully supported throughout BWA. Ideally, a value 0 for disabling all the output to stderr; 1 for outputting errors only; 2 for warnings and errors; 3 for all normal messages; 4 or higher for debugging. When this option takes value 4, the output is not SAM. ')
    parser.add_argument('-r', '--reference', type=str)
    parser.add_argument('-i', '--inputfile', type=str)
    parser.add_argument('-o', '--outputfile', type=str)
    opts = parser.parse_args()

    THREADS = opts.THREADS
    Minimum_seed_length = opts.Minimum_seed_length
    Mismatch_penalty = opts.Mismatch_penalty
    Gap_open_penalty = opts.Gap_open_penalty
    verbose = opts.verbose
    reference = opts.reference
    input_file = opts.inputfile
    output_file = opts.outputfile
    
    cmd = 'bwa mem -t ' +THREADS+' -k '+Minimum_seed_length+' -B '+Mismatch_penalty+' -O '+Gap_open_penalty+' -v '+verbose+' '+reference+' '+input_file+' > '+ output_file
    
    os.system(cmd)
    #print(cmd)
        
if __name__ == "__main__":
    main()
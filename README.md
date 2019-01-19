
# Transcription-Factor-DNA-binding assay analysis pipeline

The Dap-Seq assay can be used to determine protein binding sites on reference genome; it's very similar to Chipseq TF assay but has much better specificity and the implementation is more efficient. This pipeline was designed specifically for analysing Dap-seq result by combining peak signals from two popular peaking calling tools: MACS2 and GEM, and using meme suite for motif model building and binding site targeting.

Protocols for weblab experiment can be found at:
https://www.nature.com/articles/nprot.2017.055

Flowchart of this impelemented pipeline

<img src='./images/flowchart.png' width=800 >

Here is a quick review of the output from this pipeline.(left) predicted motif model (right) size of the circles are representative of the peaks called by MACS2 and GEM, as well as motif discovered via meme suite. The ovrlap shows the number of peaks/motif loci matches.

<img src='./images/output.png' width=1000 >

bigwig and gff files for peak/motif binding site visualization in IGV or other compatible tools are in the zip file generated at the end of this pipeline.


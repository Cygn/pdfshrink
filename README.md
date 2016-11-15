# pdfshrink

Usage: pdfshrink [-sepP | --screen --ebook --printer --prepress] infile [outfile]

A bash script to reduce the size of a pdf file, by optimizations offered by ghostscript. 
Four different levels are available, which will mainly affect the dpi of included images:

*screen 72 dpi
*ebook 150 dpi
*priter: 300 dpi
*prepress 300 dpi + better colors

the default is screen (worst quality, best reduction)

if outfile is not specified, it will be infile.shrink.pdf. 

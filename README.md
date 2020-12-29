# pdfshrink

Available as __rpm__ at [https://copr.fedorainfracloud.org/coprs/cygn/pdfshrink/](https://copr.fedorainfracloud.org/coprs/cygn/pdfshrink/)

------------------------------

Usage: *pdfshrink [-sepP | --screen --ebook --printer --prepress] infile [outfile]*

A simple script to reduce the size of a pdf file, by optimizations offered by ghostscript. 
Four different levels are available, which will mainly affect the dpi of included images:

* screen 72 dpi
* ebook 150 dpi
* printer: 300 dpi
* prepress 300 dpi + colors

It doesn't give smaller files in every case, but often does, **even when there are no images nor graphics**. If an image appears several times in the original file the reduction can be quite substantial. The default is *screen* (worst quality, best reduction). 
Metadata is kept and it produces a PDF1.4 compatible file. If *outfile* is not specified, it will be *infile.shrink.pdf*. 

Name:           pdfshrink
Version:        1.0
Release:        2
Summary:        A script to compress the size of pdf files

Group:          script
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/cygn/pdfshrink.git
Source0:        pdfshrink-1.0.tar.gz
Vendor:         Sinan H <sinan@haliyo.net>
Packager:       Sinan H <sinan@haliyo.net>

Requires: 	    ghostscript

Summary:        A simple script to reduce the size of a pdf file, by optimizations offered by ghostscript. Four different levels are available, which will mainly affect the dpi of included images.

%description
A simple script to reduce the size of a pdf file, by optimizations offered by ghostscript. Four different levels are available, which will mainly affect the dpi of included images.
It doesn't give smaller files in every case, but often does, **even when there are no images nor graphics**. If an image appears several times in the original file the reduction can be quite substantial. The default is *screen* (worst quality, best reduction). 
Metadata is kept and it produces a PDF1.4 compatible file. If *outfile* is not specified, it will be *infile.shrink.pdf*. 

Usage: *pdfshrink [-sepP | --screen --ebook --printer --prepress] infile [outfile]*

- screen 72 dpi
- ebook 150 dpi
- printer: 300 dpi
- prepress 300 dpi + colors



%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin/
install -m 0755 pdfshrink $RPM_BUILD_ROOT/usr/bin/pdfshrink

%files
/usr/bin/pdfshrink
%doc README.md
%license LICENSE

%changelog
* Sat Dec 26 2020 Sinan H  1.0.0
  - Initial rpm release


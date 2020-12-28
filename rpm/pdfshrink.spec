Name:           pdfshrink
Version:        1
Release:        0
Summary:        A script to compress the size of pdf files

Group:          script
BuildArch:      noarch
License:        GPL
URL:            https://github.com/cygn/pdfshrink.git
Source0:        pdfshrink-1.0.tar.gz

%description
A simple script to reduce the size of a pdf file, by optimizations offered by ghostscript. Four different levels are available, 
which will mainly affect the dpi of included images.

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin/
install -m 0755 pdfshrink $RPM_BUILD_ROOT/usr/bin/pdfshrink

%files
/usr/bin/pdfshrink

%changelog
* Sat Dec 26 2020 Sinan H  1.0.0
  - Initial rpm release


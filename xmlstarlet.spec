Summary:	Command Line XML Toolkit
Name:		xmlstarlet
Version:	1.0.1
Release:	1
License:	MIT
Group:		Applications/Publishing/XML
Source0:	http://xmlstar.sourceforge.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	8deb71834bcdfb4443c258a1f0042fce
Patch0:		%{name}-nostatic.patch
URL:		http://xmlstar.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLStarlet is a set of command line utilities which can be used to
transform, query, validate, and edit XML documents and files using
simple set of shell commands in similar way it is done for plain text
files using UNIX grep, sed, awk, diff, patch, join, etc commands.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README Copyright TODO doc/xmlstarlet.txt doc/xmlstarlet.pdf
%{_mandir}/man1/xmlstarlet.1*
%attr(755,root,root) %{_bindir}/xml

Summary:	Command Line XML Toolkit
Summary(pl.UTF-8):	Zestaw obsługiwanych z linii poleceń narzędzi do XML-a
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
BuildRequires:	libxml2-devel >= 1:2.6.12
BuildRequires:	libxslt-devel >= 1.1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLStarlet is a set of command line utilities which can be used to
transform, query, validate, and edit XML documents and files using
simple set of shell commands in similar way it is done for plain text
files using UNIX grep, sed, awk, diff, patch, join, etc commands.

%description -l pl.UTF-8
XMLStarlet to zestaw obsługiwanych z linii poleceń narzędzi, których
można używać do przekształcania, odpytywania, sprawdzania poprawności
i modyfikowania dokumentów i plików XML przy użyciu prostego zbioru
poleceń powłoki podobnie jak robi się to z plikami czysto tekstowymi
przy użyciu poleceń uniksowych grep, sed, awk, diff, patch, join itp.

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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README Copyright TODO doc/xmlstarlet.txt doc/xmlstarlet.pdf
%attr(755,root,root) %{_bindir}/xml
%{_mandir}/man1/xmlstarlet.1*

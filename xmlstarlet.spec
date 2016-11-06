Summary:	Command Line XML Toolkit
Summary(pl.UTF-8):	Zestaw obsługiwanych z linii poleceń narzędzi do XML-a
Name:		xmlstarlet
Version:	1.6.1
Release:	1
License:	MIT
Group:		Applications/Publishing/XML
Source0:	http://downloads.sourceforge.net/xmlstar/%{name}-%{version}.tar.gz
# Source0-md5:	f3c5dfa3b1a2ee06cd57c255cc8b70a0
URL:		http://xmlstar.sourceforge.net/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	libxslt-devel >= 1.1.9
Requires:	libxml2 >= 1:2.6.27
Requires:	libxslt >= 1.1.9
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

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# rename to what is expected, keep "xml" name for compatibility
ln $RPM_BUILD_ROOT%{_bindir}/xml $RPM_BUILD_ROOT%{_bindir}/xmlstarlet

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README Copyright TODO doc/xmlstarlet.txt doc/xmlstarlet-ug.pdf
%attr(755,root,root) %{_bindir}/xml
%attr(755,root,root) %{_bindir}/xmlstarlet
%{_mandir}/man1/xmlstarlet.1*

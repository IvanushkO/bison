Summary:	A GNU general-purpose parser generator
Summary(de):	GNU-Parser-Generator
Summary(fr):	G�n�rateur d'analyseur lexical de GNU
Summary(pl):	GNU generator sk�adni 
Summary(tr):	GNU ayr��t�r�c� �reticisi
Name:		bison
Version:	1.28
Release:	8
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	%{name}.1.pl
Patch0:		%{name}-info.patch
Patch1:		%{name}-man.patch
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	yacc

%define		_datadir	/usr/share/misc

%description
Bison is a general purpose parser generator which converts a grammar
description for an LALR context-free grammar into a C program to parse
that grammar. Bison can be used to develop a wide range of language
parsers, from ones used in simple desk calculators to complex
programming languages. Bison is upwardly compatible with Yacc, so any
correctly written Yacc grammar should work with Bison without any
changes. If you know Yacc, you shouldn't have any trouble using Bison
(but you do need to be very proficient in C programming to be able to
use Bison). Many programs use Bison as part of their build process.
Bison is only needed on systems that are used for development.

%description -l de
Dies ist der GNU-Parser-Generator, der gr��tenteils mit yacc
kompatibel ist. Viele Programme benutzen ihn als Teil des
Aufbauvorgangs. Bison wird nur auf Systemen ben�tigt, die zur
Entwicklung verwendet werden.

%description -l fr
G�n�rateur d'analyseur lexical de GNU compatible avec yacc. De
nombreux programmes l'utilisent dans leur phase de construction. Bison
ne sert que sur les syst�mes utilis�s pour le d�veloppement.

%description -l pl
W pakiecie znajduje si� implementacja GNU generatora analizatora
sk�adni, kt�ry jest odpowiednikiem programu yacc. Wiele program�w
podczas kompilacji potrzebuje tego programu aby proces budowy plik�w
binarnych przebiega� prawid�owo. Bison jest potrzebny tylko w
systemach, w kt�rych prowadzone s� r�nego rodzaju kompilacje.

%description -l tr
byacc bir yacc ayr��t�r�c�s�d�r. Pek �ok program taraf�ndan, kurulum
s�reci s�ras�nda kullan�l�r. Geli�tirme yapanlara gerekli olabilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/bison.1

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/*info*
%{_datadir}/*

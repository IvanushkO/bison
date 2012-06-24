Summary:	A GNU general-purpose parser generator
Summary(de):	GNU-Parser-Generator
Summary(es):	Generador de parser de la GNU
Summary(fr):	G�n�rateur d'analyseur lexical de GNU
Summary(pl):	GNU generator sk�adni
Summary(pt_BR):	Gerador de parser da GNU
Summary(ru):	Bison - ��������� �������� GNU
Summary(tr):	GNU ayr��t�r�c� �reticisi
Summary(uk):	Bison - ��������� �����Ҧ� GNU
Name:		bison
Version:	1.875
Release:	4
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5: b7f8027b249ebd4dd0cc948943a71af0
Source1:	%{name}.1.pl
Patch0:		%{name}-info.patch
Patch1:		%{name}-unused.patch
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pkgdatadir	%{_datadir}/bison

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

%description -l es
Este es el creador de an�lisis gramatical GNU m�s compatible con yacc.
Varios programas lo utilizan como parte del su proceso de
construcci�n. Bison solamente hace falta en sistemas que se usan para
desarrollo.

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

%description -l pt_BR
Este � o gerador de an�lise gramatical GNU que � mais compat�vel com
yacc. V�rios programas o utilizam como parte do seu processo de
constru��o. Bison � somente necess�rio em sistemas que s�o usados para
desenvolvimento.

%description -l ru
Bison - ��� ������, � �������� ����������� � yacc. ������ ���������
���������� ��� � �������� �����������. Bison ����� ������ � ��������,
������� ������������ ��� ���������� ��������.

%description -l tr
byacc bir yacc ayr��t�r�c�s�d�r. Pek �ok program taraf�ndan, kurulum
s�reci s�ras�nda kullan�l�r. Geli�tirme yapanlara gerekli olabilir.

%description -l uk
Bison - �� ������, ���¦������ ��ͦ���� � yacc. ������ �������
�������������� ���� � �����Ӧ ���Ц��æ�. Bison ���Ҧ��� Ԧ���� �
��������, �˦ ���������������� ��� �������� �������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make} \
	pkgdatadir=%{pkgdatadir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdatadir=%{pkgdatadir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/bison.1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bison
%{pkgdatadir}
%{_libdir}/lib*.a
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/*.info*

# revision 31990
# category Package
# catalog-ctan /graphics/pstricks/contrib/pedigree/pedigree-perl
# catalog-date 2012-05-31 18:08:53 +0200
# catalog-license gpl2
# catalog-version 1.0
Name:		texlive-pedigree-perl
Version:	1.0
Release:	9
Summary:	Generate TeX pedigree files from CSV files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pedigree/pedigree-perl
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pedigree-perl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pedigree-perl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-pedigree-perl.bin = %{EVRD}

%description
This program generates TeX commands to typeset pedigrees --
either TeX fragments or full LaTeX files, to be processed by
the authors' pst-pdgr package. The program has support for
multilanguage pedigrees (at the present moment the English and
Russian languages are supported).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/pedigree
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/AbortionNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/Area.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/ChildlessNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/Language.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/MarriageNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/Node.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/Parser.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/PersonNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/TwinsNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/pedigree.pl
%doc %{_mandir}/man1/pedigree.1*
%doc %{_texmfdistdir}/doc/man/man1/pedigree.man1.pdf
%doc %{_texmfdistdir}/doc/support/pedigree-perl/LICENSE
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Makefile
%doc %{_texmfdistdir}/doc/support/pedigree-perl/NEWS
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/AbortionNode.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Area.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/ChildlessNode.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Language.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Makefile
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/MarriageNode.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Node.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Parser.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/PersonNode.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/TwinsNode.3
%doc %{_texmfdistdir}/doc/support/pedigree-perl/README
%doc %{_texmfdistdir}/doc/support/pedigree-perl/doc/Makefile
%doc %{_texmfdistdir}/doc/support/pedigree-perl/doc/abortions.tex
%doc %{_texmfdistdir}/doc/support/pedigree-perl/doc/english.tex
%doc %{_texmfdistdir}/doc/support/pedigree-perl/doc/english1.tex
%doc %{_texmfdistdir}/doc/support/pedigree-perl/doc/pedigree.bib
%doc %{_texmfdistdir}/doc/support/pedigree-perl/doc/pedigree.pdf
%doc %{_texmfdistdir}/doc/support/pedigree-perl/doc/pedigree.ps
%doc %{_texmfdistdir}/doc/support/pedigree-perl/doc/pedigree.tex
%doc %{_texmfdistdir}/doc/support/pedigree-perl/doc/russian.tex
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/abortions.csv
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/badsort.csv
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/childlessness.csv
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/consanguinic.csv
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/english.cfg
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/english.csv
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/english1.cfg
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/english_short.cfg
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/pedigree.cfg
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/russian.cfg
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/russian.csv
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/sort1.csv
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/sort2.csv
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/sort3.csv
%doc %{_texmfdistdir}/doc/support/pedigree-perl/examples/twins.csv

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/pedigree-perl/pedigree.pl pedigree
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


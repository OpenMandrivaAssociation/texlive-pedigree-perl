Name:		texlive-pedigree-perl
Version:	64227
Release:	2
Summary:	Generate TeX pedigree files from CSV files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pedigree/pedigree-perl
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pedigree-perl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pedigree-perl.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/scripts/pedigree-perl
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/support/pedigree-perl

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

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

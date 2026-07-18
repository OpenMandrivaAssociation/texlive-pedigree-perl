%global tl_name pedigree-perl
%global tl_revision 64227
%global tl_bin_links pedigree:%{_texmfdistdir}/scripts/pedigree-perl/pedigree.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Generate TeX pedigree files from CSV files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pedigree/pedigree-perl
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pedigree-perl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pedigree-perl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pedigree-perl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pedigree-perl.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This program generates TeX commands to typeset pedigrees -- either TeX
fragments or full LaTeX files, to be processed by the authors' pst-pdgr
package. The program has support for multilanguage pedigrees (at the
present moment the English and Russian languages are supported).


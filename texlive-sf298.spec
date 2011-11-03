# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sf298
# catalog-date 2007-01-14 22:06:18 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-sf298
Version:	1.2
Release:	1
Summary:	Standard form 298
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sf298
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sf298.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sf298.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sf298.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A LaTeX package for generating a completed standard form 298
(Rev. 8-98) as prescribed by ANSI Std. Z39.18 for report
documentation as part of a document delivered, for instance, on
a U.S. government contract.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sf298/sf298.sty
%doc %{_texmfdistdir}/doc/latex/sf298/sample298.pdf
%doc %{_texmfdistdir}/doc/latex/sf298/sample298.tex
%doc %{_texmfdistdir}/doc/latex/sf298/sf298.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sf298/Makefile
%doc %{_texmfdistdir}/source/latex/sf298/sf298.dtx
%doc %{_texmfdistdir}/source/latex/sf298/sf298.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

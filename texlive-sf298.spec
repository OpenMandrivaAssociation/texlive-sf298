Name:		texlive-sf298
Version:	41653
Release:	1
Summary:	Standard form 298
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sf298
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sf298.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sf298.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sf298.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for generating a completed standard form 298
(Rev. 8-98) as prescribed by ANSI Std. Z39.18 for report
documentation as part of a document delivered, for instance, on
a U.S. government contract.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sf298
%doc %{_texmfdistdir}/doc/latex/sf298
#- source
%doc %{_texmfdistdir}/source/latex/sf298

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

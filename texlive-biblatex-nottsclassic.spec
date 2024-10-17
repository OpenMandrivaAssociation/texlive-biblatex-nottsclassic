Name:		texlive-biblatex-nottsclassic
Version:	41596
Release:	2
Summary:	Citation style for the University of Nottingham
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-nottsclassic
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-nottsclassic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-nottsclassic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This citation-style covers the citation and bibliography rules
of the University of Nottingham.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-nottsclassic
%doc %{_texmfdistdir}/doc/latex/biblatex-nottsclassic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

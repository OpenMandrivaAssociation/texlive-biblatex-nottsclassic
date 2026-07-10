%global tl_name biblatex-nottsclassic
%global tl_revision 41596

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Citation style for the University of Nottingham
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-nottsclassic
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-nottsclassic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-nottsclassic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This citation-style covers the citation and bibliography rules of the
University of Nottingham.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-nottsclassic
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-nottsclassic
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-nottsclassic/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-nottsclassic/nottsclassic.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-nottsclassic/nottsclassic.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-nottsclassic/nottsclassic-english.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-nottsclassic/nottsclassic.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-nottsclassic/nottsclassic.cbx

Summary:	Advanced tail
Summary(pl):	Rozbudowany tail
Name:		multitail
Version:	3.3.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.vanheusden.com/%{name}/%{name}-%{version}.tgz
# Source0-md5:	b35691f8708ad00ddf3fd18beb56a334
URL:		http://www.vanheusden.com/multitail/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multitail lets you view one or multiple files like the original tail
program. The difference is that it creates multiple windows on your
console (with ncurses). It can also use colors while displaying the
logfiles, for faster recognition of which lines are important and
which are not. It supports regular expressions. It has interactive
menus for editing given regular expressions and deleting and adding
windows.

%description -l pl
multitail pozwala ogl±daæ jeden lub wiêcej plików podobnie jak
oryginalny program tail. Ró¿nica jest taka, ¿e tworzy wiele okien
na terminalu (z u¿yciem ncurses). Mo¿e tak¿e u¿ywaæ kolorów przy
wy¶wietlaniu plików logów w celu szybszego odró¿nienia, które linie s±
wa¿ne, a które nie. Obs³uguje wyra¿enia regularne. Ma interaktywne
menu do edycji podanych wyra¿eñ regularnych oraz usuwania i dodawania
okien.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="-DLinux -DVERSION=\\\"%{version}\\\" -Wall %{rpmcflags} -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1}

install multitail $RPM_BUILD_ROOT%{_bindir}
install multitail.1 $RPM_BUILD_ROOT%{_mandir}/man1
install multitail.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes readme.txt manual.html
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

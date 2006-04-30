Summary:	Advanced tail
Summary(pl):	Rozbudowany tail
Name:		multitail
Version:	4.0.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.vanheusden.com/multitail/%{name}-%{version}.tgz
# Source0-md5:	b6017e19aa7cf7e2b4fddd75a596a1a7
URL:		http://www.vanheusden.com/multitail/
BuildRequires:	ncurses-ext-devel
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
multitail pozwala ogl�da� jeden lub wi�cej plik�w podobnie jak
oryginalny program tail. R�nica jest taka, �e tworzy wiele okien na
terminalu (z u�yciem ncurses). Mo�e tak�e u�ywa� kolor�w przy
wy�wietlaniu plik�w log�w w celu szybszego odr�nienia, kt�re linie s�
wa�ne, a kt�re nie. Obs�uguje wyra�enia regularne. Ma interaktywne
menu do edycji podanych wyra�e� regularnych oraz usuwania i dodawania
okien.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-DLinux -DVERSION=\\\"%{version}\\\" -Wall %{rpmcflags} -I/usr/include/ncurses -DCONFIG_FILE=\\\"%{_sysconfdir}/%{name}.conf\\\""

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

Summary:	Advanced tail
Summary(pl):	Rozbudowany tail
Name:		multitail
Version:	2.6
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.vanheusden.com/%{name}/%{name}-%{version}.tgz
# Source0-md5:	f7c53cf2bc01c9f489045f4f2f8823ba
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
multitail pozwala ogl�da� jeden lub wi�cej plik�w podobnie jak
oryginalny program tail. R�nica jest taka, �e tworzy wiele okien
na terminalu (z u�yciem ncurses). Mo�e tak�e u�ywa� kolor�w przy
wy�wietlaniu plik�w log�w w celu szybszego odr�nienia, kt�re linie s�
wa�ne, a kt�re nie. Obs�uguje wyra�enia regularne. Ma interaktywne
menu do edycji podanych wyra�e� regularnych oraz usuwania i dodawania
okien.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="-Wall %{rpmcflags} -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install multitail $RPM_BUILD_ROOT%{_bindir}
install multitail.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes readme.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

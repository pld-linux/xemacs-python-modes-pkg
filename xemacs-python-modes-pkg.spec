%define 	srcname	python-modes
Summary:	XEmacs modes for Python programming languages
Summary(pl):	XEmacsowe tryby Pythona 
Name:		xemacs-%{srcname}-pkg
Version:	1.06
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	ecda2909abf566525b9c2e7bc6c58e54
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	python
Requires:	xemacs
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-devel-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XEmacs modes for Python programming languages. Includes pydoc support.


%description -l pl
Tryb XEmacsa do Pythona wraz z interfejsem do pydoc

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

install -d $RPM_BUILD_ROOT/%{py_sitedir}
cp lisp/python-modes/*py $RPM_BUILD_ROOT/%{py_sitedir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/python-modes/{ChangeLog,pydoc-el-README}
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_datadir}/xemacs-packages/lisp/*/*.py
%{py_sitedir}/*.pyc
%{py_sitedir}/*.pyo
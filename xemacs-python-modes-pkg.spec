%define 	srcname	python-modes
Summary:	XEmacs modes for Python programming languages
Summary(pl.UTF-8):	XEmacsowe tryby Pythona
Name:		xemacs-%{srcname}-pkg
Version:	1.07
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	574cac0c86f8e19c684017989ea25801
URL:		http://www.xemacs.org/
BuildRequires:	python-modules
Requires:	python
Requires:	xemacs
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-devel-pkg
Requires:	xemacs-base-pkg
Conflicts:	xemacs-sumo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XEmacs modes for Python programming languages. Includes pydoc support.

%description -l pl.UTF-8
Tryb XEmacsa do Pythona wraz z interfejsem do pydoc.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/python-modes/{ChangeLog,pydoc-el-README}
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*

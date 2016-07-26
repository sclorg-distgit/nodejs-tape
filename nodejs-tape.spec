# spec file for package nodejs-nodejs-tape
%{?scl:%scl_package nodejs-nodejs-tape}
%{!?scl:%global pkg_name %{name}}

%global npm_name tape
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-tape
Version:	4.0.3
Release:	7%{?dist}
Summary:	Tap-producing test harness for node and browsers
Url:		https://github.com/substack/tape
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm}} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(concat-stream)
BuildRequires:	npm(falafel)
BuildRequires:	npm(tap)
%endif

%description
Tap-producing test harness for node and browsers

%prep
%setup -q -n package

%nodejs_fixdep inherits 2.0.0
%nodejs_fixdep defined 1.0.0
%nodejs_fixdep deep-equal
%nodejs_fixdep resumer

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr bin/ lib/ package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

#rm -f %{buildroot}%{_bindir}/tape
mkdir -p %{buildroot}%{_bindir}/tape
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/tape %{buildroot}%{_bindir}/tape
%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/tape
%{_bindir}/tape

%doc readme.markdown LICENSE

%changelog
* Thu Feb 11 2016 Tomas Hrcka <thrcka@redhat.com> - 4.0.3-7
- Fix simlink to bindir to point to file not directory

* Mon Dec 07 2015 Tomas Hrcka <thrcka@redhat.com> - 4.0.3-5
- Remove fixdep macro for dependency on glob package

* Tue Sep 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.3-3
- Add missing files to %%install

* Thu Aug 20 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.3-2
- Add %%nodejs_fixdep macros

* Tue Aug 11 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.3-1
- Initial build

Name:          container-exception-logger
Version:       1.0.3
Release:       2
Summary:       Logging from a container to a host
License:       GPLv3+
URL:           https://github.com/abrt/container-exception-logger
Source0:       %{name}-%{version}.tar.gz
BuildRequires: asciidoc libxslt

%description
Container-exception-logger is a tool designed to run inside of a container
which is able to get its input outside of the container.

%package help
Summary: Help document for the %{name} package

%description help
Help document for the %{name} package.

%prep
%autosetup -n %{name}-%{version} -p1

%build
gcc %{optflags} src/%{name}.c -o src/container-exception-logger
a2x -d manpage -f manpage man/container-exception-logger.1.asciidoc

%install
install -d %{buildroot}%{_bindir}
cp src/container-exception-logger %{buildroot}/%{_bindir}/container-exception-logger

install -d %{buildroot}/%{_mandir}/man1
cp man/container-exception-logger.1 %{buildroot}/%{_mandir}/man1/container-exception-logger.1

%files
%license COPYING
%attr(6755, root, root) %{_bindir}/container-exception-logger

%files help
%{_mandir}/man1/container-exception-logger.1.*

%changelog
* Thu Dec 12 2019 shijian <shijian16@huawei.com> 1.0.3-2
- Package init

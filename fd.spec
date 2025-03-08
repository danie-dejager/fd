%define name fd
%define version 10.2.0
%define release 2%{?dist}

Summary:  A simple, fast and user-friendly alternative to 'find' 
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  MIT License
URL:      https://github.com/sharkdp/fd
Source0:  https://github.com/sharkdp/fd/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: curl
BuildRequires: gcc
BuildRequires: make
BuildRequires: gzip
BuildRequires: upx

%description
fd is a program to find entries in your filesystem. It is a simple, fast and user-friendly alternative to find. While it does not aim to support all of find's powerful functionality, it provides sensible (opinionated) defaults for a majority of use cases.

%prep
%setup -q -n fd-%{version}

%build
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release --locked
strip --strip-all target/release/%{name}
mkdir -p %{buildroot}/%{_bindir}
gzip doc/fd.1

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}/%{_sysconfdir}/zsh/site-functions/

install -Dpm 0644 doc/%{name}.1.gz -t %{buildroot}%{_mandir}/man1/
install -m 755 target/release/%{name} %{buildroot}/%{_bindir}/
install -Dpm 0644 contrib/completion/_%{name} -t %{buildroot}/%{_sysconfdir}/zsh/site-functions/

%files
%doc README.md
%{_bindir}/%{name}
%{_sysconfdir}/zsh/site-functions/_%{name}
%{_mandir}/man1/%{name}.1.gz

%define name fd
%define version 10.2.0
%define release 1%{?dist}

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

%install
mkdir -p %{buildroot}/%{_bindir}/

install -m 755 target/release/fd %{buildroot}/%{_bindir}/

%files
%doc README.md
%{_bindir}/fd

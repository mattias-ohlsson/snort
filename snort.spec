%global commit 5dd2afc059f215aed5001a540f949d9866fedcae
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           snort
Version:        3.0.0
Release:        1.git.%{shortcommit}%{?dist}
Summary:        An open source Network Intrusion Detection System

License:        GPLv2+
URL:            https://www.snort.org
Source0:        https://github.com/snort3/snort3/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libdnet-devel
BuildRequires:  hwloc-devel
BuildRequires:  openssl-devel
BuildRequires:  libpcap-devel
BuildRequires:  xz-devel
BuildRequires:  libuuid-devel
BuildRequires:  flatbuffers-devel
BuildRequires:  hyperscan-devel
BuildRequires:  gperftools-devel
BuildRequires:  libdaq-devel
BuildRequires:  luajit-devel

%description
Snort is an open source intrusion prevention system capable of real-time
traffic analysis and packet logging.

%prep
%autosetup -n snort3-%{commit}

%build
./configure_cmake.sh --disable-static-daq --prefix=%{_prefix} --enable-tcmalloc
cd build/
%make_build

%install
rm -rf $RPM_BUILD_ROOT
cd build/
%make_install

%files
%license COPYING LICENSE
%doc README.md
%{_bindir}/appid_detector_builder.sh
%{_bindir}/fbstreamer
%{_bindir}/%{name}
%{_bindir}/snort2lua
%{_bindir}/u2boat
%{_bindir}/u2spewfoo
%{_prefix}/etc/%{name}/*.lua
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}/daqs/*.so
%{_docdir}/%{name}/*

%changelog
* Thu Jan 30 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.0.0-1
- Initial build

%bcond_without check
%global debug_package %{nil}

%global crate env_logger

Name:           rust-%{crate}
Version:        0.8.3
Release:        2
Summary:        Logging implementation for `log` which is configured via environment variable

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/env_logger
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Logging implementation for `log` which is configured via an environment
variable.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+atty-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atty-devel %{_description}

This package contains library source intended for building other packages
which use "atty" feature of "%{crate}" crate.

%files       -n %{name}+atty-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+humantime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+humantime-devel %{_description}

This package contains library source intended for building other packages
which use "humantime" feature of "%{crate}" crate.

%files       -n %{name}+humantime-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages
which use "regex" feature of "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+termcolor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+termcolor-devel %{_description}

This package contains library source intended for building other packages
which use "termcolor" feature of "%{crate}" crate.

%files       -n %{name}+termcolor-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

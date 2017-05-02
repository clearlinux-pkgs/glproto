#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glproto
Version  : 1.4.17
Release  : 9
URL      : http://xorg.freedesktop.org/releases/individual/proto/glproto-1.4.17.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/proto/glproto-1.4.17.tar.gz
Summary  : GL extension headers
Group    : Development/Tools
License  : SGI-B-2.0
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(xorg-macros)

%description
OpenGL Extension to the X Window System
This extension defines a protocol for the client to send 3D rendering
commands to the X server.

%package dev
Summary: dev components for the glproto package.
Group: Development
Provides: glproto-devel

%description dev
dev components for the glproto package.


%package dev32
Summary: dev32 components for the glproto package.
Group: Default

%description dev32
dev32 components for the glproto package.


%prep
%setup -q -n glproto-1.4.17
pushd ..
cp -a glproto-1.4.17 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/GL/glxint.h
/usr/include/GL/glxmd.h
/usr/include/GL/glxproto.h
/usr/include/GL/glxtokens.h
/usr/include/GL/internal/glcore.h
/usr/lib64/pkgconfig/glproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32glproto.pc

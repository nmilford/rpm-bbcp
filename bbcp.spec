# Copyright 2013, Nathan Milford
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# To Install:
# sudo yum -y install rpmdevtools && rpmdev-setuptree
# wget https://raw.github.com/nmilford/rpm-bbcp/master/bbcp.spec -O ~/rpmbuild/SPECS/bbcp.spec
# wget http://www.slac.stanford.edu/~abh/bbcp/bin/amd64_rhel50/bbcp -O ~/rpmbuild/SOURCES/bbcp
# rpmbuild -bb ~/rpmbuild/SPECS/bbcp.spec

# Valid platform options are
# amd64_linux26 amd64_rhel50 amd64_rhel60
# i386_linux26  i386_rhel50  i386_rhel60
%define bbcp_platform amd64_rhel50

Name:      bbcp
Version:   12.08.17.00.0
Release:   1
Summary:   A point-to-point network file copy application.
License:   Stanford
URL:       http://www.slac.stanford.edu/~abh/bbcp/
Group:     Applications/Communications
Source0:   http://www.slac.stanford.edu/~abh/bbcp/bin/%{platform}/%{name}
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Packager:  Nathan Milford <nathan@milford.io>

%description
bbcp is a point-to-point network file copy application written by Andy
Hanushevsky at SLAC as a tool for the BaBar collaboration. It is capable of
transferring files at approaching line speeds in the WAN.

%prep

%build
rm -rf %{buildroot}

%{__cat} <<EOF > %_sourcedir/LICENSE
Copyright © 2002-2012, Board of Trustees of the Leland Stanford, Jr. University.
Produced under contract DE-AC02-76-SF00515 with the US Department of Energy.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

a.      Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
b.      Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
c.       Neither the name of the Leland Stanford, Jr. University nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
EOF

%install
install -d -m 755 %{buildroot}/%{_sbindir}
install    -m 755 %_sourcedir/%{name} %{buildroot}/%{_sbindir}

install -d -m 755 %{buildroot}/usr/share/doc/%{name}
install    -m 644 %_sourcedir/LICENSE %{buildroot}/%{_defaultdocdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/%{name}
%{_defaultdocdir}/%{name}/LICENSE

%changelog
* Wed Aug 14 2013 Nathan Milford <nathan@milford.io> 0.1.0-1
- Initial spec.
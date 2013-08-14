rpm-bbcp
========

An RPM spec file to install bbcp.


To Install:
`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`wget https://raw.github.com/nmilford/rpm-bbcp/master/bbcp.spec -O ~/rpmbuild/SPECS/bbcp.spec`

`wget http://www.slac.stanford.edu/~abh/bbcp/bin/amd64_rhel50/bbcp -O ~/rpmbuild/SOURCES/bbcp`

`rpmbuild -bb ~/rpmbuild/SPECS/bbcp.spec`
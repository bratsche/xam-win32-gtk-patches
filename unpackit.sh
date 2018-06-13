#!/bin/sh

rpm2cpio /var/tmp/build-root/home/abuild/rpmbuild/RPMS/noarch/mingw32-gtk2-2.24.22-0.noarch.rpm | cpio -i -d

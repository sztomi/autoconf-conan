from __future__ import print_function
from conans import ConanFile, CMake, tools
from glob import glob
from time import sleep

import os
import subprocess

class AutoConfConan(ConanFile):
    name = 'autoconf'
    version = '2.69'
    license = 'MIT'
    url = 'https://github.com/sztomi/libtool-conan'
    description = 'This is a tooling package for GNU automake'
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = 'm4/latest@sztomi/testing'
    generators = 'cmake', 'virtualenv'

    def source(self):
        tarball_url = 'https://gnu.cu.be/autoconf/autoconf-{}.tar.gz'.format(self.version)
        tgz = tarball_url.split('/')[-1]
        tools.download(tarball_url, tgz)
        tools.untargz(tgz)
        os.unlink(tgz)

    def build(self):
        self.dirname = glob('autoconf-*')[0]
        os.chdir(self.dirname)        
        def run_in_env(cmd):
            activate = '. ../activate.sh &&'
            self.run(activate + cmd)
        run_in_env('./configure --prefix={}'.format(self.package_folder))
        self.run('make')
        self.run('make install')

    def package(self):
        pass

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, 'bin'))
        

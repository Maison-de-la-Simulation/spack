# Copyright (C) 2020 Commissariat a l'energie atomique et aux energies alternatives (CEA)
# and others. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pdi(CMakePackage):
    """PDI is a library that aims to decouple high-performance simulation codes
    from Input/Output concerns. It offers a declarative application programming
    interface that enables codes to expose the buffers in which they store data
    and to notify PDI of significant steps of the simulation. It supports a
    plugin system to make existing libraries such as HDF5, SIONlib or FTI
    available to codes, potentially mixed in a single execution."""

    homepage = "https://pdi.julien-bigot.fr/"
    url = "https://gitlab.maisondelasimulation.fr/pdidev/pdi/-/archive/1.3.1/pdi-1.3.1.tar.bz2"
    git = "https://gitlab.maisondelasimulation.fr/pdidev/pdi.git"

    maintainers = ['jbigot']

    version('develop', branch='master', no_cache=True)
    version('1.4.3',   sha256='b7f049cae9e6fb0ddba3a458e15d6f1578876663c04b18f62b052f9698750974')
    version('1.4.2',   sha256='b252d5098f3b13b5d883265597f567aa0aa423c95fe4a10554772d485ce37e86')
    version('1.4.1',   sha256='55e17629ca373232a8a2530c4ad83403729c74fbe4fcbcfc32e8128800cb40a4')
    version('1.4.0',   sha256='1c273d39df14f44ccb3e6d0fc36f88c19fff7a3f819e7d6d6c80b5ac9eed033b')
    version('1.3.1',   sha256='a4a1f9d4d6ca6790487edf65e3d7c9f5a5d17fb0bcdf81dfab94efc854fcc387')
    version('1.3.0',   sha256='86947c40f025a09ab228360fa002f7241801f5fb70c75f815210d607cf30b200')
    version('1.2.2',   sha256='b93a9165d4b9f1e09790c9be3c950530537cf9a9dc01210afc77e411939bdf41')
    version('1.2.1',   sha256='0c90294fb2bb9ca5f6b957d9d8f68f3a3039fc256ba92f7e5bbe316768b43037')
    version('1.2.0',   sha256='8d5821d473140ea48036e8f03668bf6295d06f8b7561d464cc1b5748bf8d2aa3')
    version('1.1.0',   sha256='8f8a33e1538afde81bb2bbbc3ba8fe3942f0824672a364d0eb2055a0255e8b0c')
    version('1.0.1',   sha256='c35f6d19cecfc3963c08c8d516386c1cd782fcdbe4e39aa91dd01376d2346cb6')
    version('1.0.0',   sha256='57f5bfd2caa35de144651b0f4db82b2a403997799c258ca3a4e632f8ff2cfc1b')
    version('0.6.5',   sha256='a1100effb62d43556bd5e50d82f51e51710dbafc8d85c5a2e03ba7c168460be9')

    variant('docs',    default=False, description='Build documentation')
    variant('tests',   default=False, description='Build tests')
    variant('fortran', default=True,  description='Enable Fortran support')
    variant('python',  default=True,  description='Enable Python support')

    depends_on('cmake@3.5:', type=('build'))
    depends_on('cmake@3.10:', type=('build'), when='+docs')
    depends_on('cmake@3.10:', type=('build'), when='+tests')
    depends_on('doxygen@1.8.13:', type=('build'), when='+docs')
    depends_on('googletest@1.8.0: +gmock', type=('link'), when='+tests')
    depends_on('paraconf +shared', type=('link', 'run'), when='-fortran')
    depends_on('paraconf +shared +fortran',type=('link', 'run'), when='+fortran')
    depends_on('pkgconfig', type=('build'))
    depends_on('python@3.7:', type=('build', 'link', 'run'), when='+python')
    depends_on('py-pybind11@2.3.0:', type=('link'), when='+python')
    depends_on('spdlog@1.3.1:', type=('link', 'run'))
    depends_on('zpp@1.0.8', type=('build'), when='+fortran')

    root_cmakelists_dir = 'pdi'

    def cmake_args(self):
        args = [
            '-DBUILD_DOCUMENTATION:BOOL={:s}'.format(
                'ON' if '+docs' in self.spec else 'OFF'),
            '-DBUILD_FORTRAN:BOOL={:s}'.format(
                'ON' if '+fortran' in self.spec else 'OFF'),
            '-DBUILD_PYTHON:BOOL={:s}'.format(
                'ON' if '+python' in self.spec else 'OFF'),
            '-DBUILD_TESTING:BOOL={:s}'.format(
                'ON' if '+tests' in self.spec else 'OFF'),
        ]
        return args

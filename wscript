#! /usr/bin/env python
# encoding: utf-8

APPNAME = 'cpp-tester'
VERSION = '0.1.0'


def build(bld):

    # Override CXXFLAGS if needed for testing
#    CXX = bld.env.get_flat("CXX")
#    if 'g++' in CXX or 'clang' in CXX:
#        if '-std=c++14' in bld.env['CXXFLAGS']:
#            bld.env['CXXFLAGS'].remove('-std=c++14')
#        bld.env.append_value('CXXFLAGS', '-std=c++1z')

    if bld.is_toplevel():

        bld.program(
            features='cxx test',
            source=bld.path.ant_glob('src/*.cpp'),
            target='cpp-tester')



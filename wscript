#! /usr/bin/env python
# encoding: utf-8

import waflib.extras.wurf_options

APPNAME = 'cpp-tester'
VERSION = '0.1.0'


def options(opt):

    opt.load('wurf_common_tools')


def resolve(ctx):

    import waflib.extras.wurf_dependency_resolve as resolve

    ctx.load('wurf_common_tools')

    ctx.add_dependency(resolve.ResolveVersion(
        name='waf-tools',
        git_repository='github.com/steinwurf/waf-tools.git',
        major=3))


def configure(conf):

    conf.load("wurf_common_tools")


def build(bld):

    bld.load("wurf_common_tools")

    CXX = bld.env.get_flat("CXX")
    # Matches both g++ and clang++
    if 'g++' in CXX or 'clang' in CXX:
        if '-std=c++11' in bld.env['CXXFLAGS']:
            bld.env['CXXFLAGS'].remove('-std=c++11')
        if '-std=gnu++11' in bld.env['CXXFLAGS']:
            bld.env['CXXFLAGS'].remove('-std=gnu++11')
        bld.env.append_value('CXXFLAGS', '-std=c++14')

    if bld.is_toplevel():

        bld.program(
            features='cxx',
            source=bld.path.ant_glob('src/*.cpp'),
            target='cpp-tester')



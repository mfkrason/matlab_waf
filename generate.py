#!/usr/bin/env python

import argparse
import os

cpp_file="""
#include <iostream>
#include "mfiles/libmy_filter.hpp"

void foo::doSomething()
{{
    std::cout << "mike was here" << std::endl;
}}
"""

hpp_file="""
#ifndef foo_hpp_
#define foo_hpp_

struct foo
{

void doSomething();

};

#endif

"""


parser = argparse.ArgumentParser()
parser.add_argument('cpp_file', type=str, help="the source file")

args = parser.parse_args()

with open(args.cpp_file, 'w') as f:
    f.write(cpp_file.format(directory=os.path.dirname(args.cpp_file)))

with open(args.cpp_file.replace('.cpp','.hpp'), 'w') as f:
    f.write(hpp_file)



from waflib import TaskGen, Task
from waflib import Options
import pprint
import os,sys

def options(opt):
    opt.load('compiler_cxx')
    opt.parser.set_defaults(prefix='{}/install'.format(os.curdir))

def configure(conf):
    conf.load('compiler_cxx')

def build(bld):
    print 'build'

    srcs = bld.path.ant_glob('src/**/*.cpp')
    srcs += bld.path.ant_glob('mfiles/**/*.m')
    print srcs
    bld(
            features='cxx cxxprogram',
            target='myTarget',
            includes=[bld.out_dir],
            source=srcs,
            )


@TaskGen.extension('.m')
def process(self, node):
    print 'process'
    tsk = self.create_task('matlab', node)
    print tsk.__class__
    tsk.run()
    print 'tsk.outputs', tsk.outputs
    self.source.extend(tsk.outputs)

class matlab(Task.Task):
    print 'matlab'

    def run(self):
        print 'executiing'
        for input in self.inputs:
            print 'input:', input
            output = 'lib{}.cpp'.format(input.name.replace('.m',''))
            print 'output', output
            print input.parent.get_bld().abspath()
            print output
            outpt = input.parent.get_bld().find_or_declare(output)
            outpt.write('\n\n')
            print outpt.abspath()
            print input.parent.get_bld()
            self.outputs.append(outpt)

            self.generator.bld.cmd_and_log('./generate.py {}'.format(outpt.abspath()))

        print self.outputs


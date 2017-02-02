#!/usr/bin/env python3

import sys
import argparse
import re
from IPython import embed

NUM_SPACES_PER_TAB = 4

parser = argparse.ArgumentParser()
parser.add_argument('--inplace','-i', action='store_true')
parser.add_argument('--backup', '-b', type=str)
parser.add_argument('file', nargs='*')
opts = parser.parse_args()

fileno = 0
if len(opts.file) > 0 and not (opts.file[0] == '-'):
    def read():
        with open(opts.file[fileno], 'r') as f:
            return f.read()
else:
    opts.file = []
    def read():
        return sys.stdin.read()

if opts.inplace or opts.backup:
    if len(opts.file) == 0:
        raise ValueError('missing file with --inplace')
    def _write(x):
        if opts.backup:
            filename = f'{opts.file[fileno]}.{opts.backup}'
        else:
            filename = f'{opts.file[fileno]}'

        with open(filename, 'w') as f:
            f.write(x)
else:
    def _write(x):
        print(x)

def write(x):
    global fileno
    _write(x)
    fileno += 1
    return fileno < len(opts.file)

func_regex = re.compile(r"^(?P<func_indent>[\ ]*)function\s*(?P<name>\w+)[\ \t]*(?P<args>\([\w\ \t,]*\))(?P<deadzone>[\s]*)(?P<comments>([\ ]*(//([^\n]*))?\n)+)[\ ]*\{", re.MULTILINE)
comment_regex = re.compile(r"^[\ \t]*//[\ \t]*", re.MULTILINE)
tab_regex = re.compile(r"^\t+",re.MULTILINE)
def transform(x):
    def _func_repl(match):
        ret = []
        func_indent = match.group('func_indent')
        name        = match.group('name')
        args        = match.group('args')
        comments    = match.group('comments')

        # remove comment prefix, indent and commented space
        comments = re.sub(comment_regex,"",comments)

        if re.match(r"^\s*$", comments) is None:
            # there are real comments to process
            lines = comments.split('\n')[:-1] # trip trailing line
            ret.append(f"{func_indent}/**")
            func_indent += ' '
            for line in lines:
                ret.append(f'{func_indent}* {line}')
            ret.append(f'{func_indent}*/')


        func_indent = func_indent[:-1]
        ret.append(f'{func_indent}function {name}{args} {{')

        return "\n".join(ret)

    def _tab_repl(match):
        return ' '*(NUM_SPACES_PER_TAB*len(match[0]))

    x = re.sub(tab_regex, _tab_repl , x)
    x = re.sub(func_regex, _func_repl, x)

    return x


while True:
    ret = write(transform(read()))
    if not ret:
        break

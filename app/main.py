import sys
import os
from pathlib import Path
from importlib import import_module

class Namespace: pass

bh = sys.bh = Namespace()

bh.CMD1=os.environ['BH_APP_NAME']
bh.THIS=Path(sys.argv[0])
bh.HERE=bh.THIS.parent
bh.DOTS_DIR=bh.HERE/'local'/'dots'
bh.SUBS_DIR=bh.HERE/'local'/'subs'
bh.dots = [x.stem for x in bh.DOTS_DIR.glob('*.py')]
bh.subs = [x.stem for x in bh.SUBS_DIR.glob('*.py')]

def parse_out_args():
    from local.parser import parser
    opts = bh.opts = parser.parse_args()
    (opts.exit == None) or exit(opts.exit)
    return opts.args

def dotted():
    args = sys.argv[1:][:]
    cmd = bh.CMD2 = args.pop()
    cmd = '.' + ( cmd[1:] or '_null' )
    cmd[1:] in bh.dots or exit( "Unknown command: '%s'" % cmd )
    foo = import_module( 'local.dots.' + cmd[1:] )
    exit( foo.main(args) )

def undotted():
    args = parse_out_args() or ['']
    cmd = bh.CMD2  = args.pop(0)
    cmd = cmd or '_null'
    cmd in bh.subs or exit( "Unknown command: '%s'" % bh.CMD2 )
    foo = import_module('local.subs.'+cmd)
    exit( foo.main(args) )

def main():
    if (sys.argv+[''])[1].startswith('.'):
        dotted()
    else:
        undotted()

if __name__=='__main__':
    main()

import sys
BH=sys.bh
DESCRIPTION="List all the subcommands and dotcommands"

from argparse import ArgumentParser

parser=ArgumentParser( prog='%s %s' % (BH.CMD1, BH.CMD2),
    description=DESCRIPTION
)

parser.add_argument(
    '--all',
    action='store_true',
    help='show plumbing'
)

def main(args):
    ARGS=parser.parse_args(args)
    args=filter(None,args)
    if ARGS.all:
        cond = lambda x : True
    else:
        cond = lambda x : not x.startswith('_')
    print( 'Subcommands:')
    for path in filter( cond, sys.bh.subs):
        print('\t' + path )
    print( '\nDotcommands:')
    for path in filter( cond, sys.bh.dots):
        print('\t.' + path )
    print('\nUse --all to include plumbing')

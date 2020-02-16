import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '--exit', action='store', type=int )
parser.add_argument( 'args', action='store', nargs='*' )
################################################################
# Every parser in the bh_tool suite must start with the above.
# All additions must go below this comment.
###############################################################


def main(args):
    print( 555, 'exit', args)
    try:
        exit( int(args.pop(0) ))
    except (IndexError, ValueError):
        exit(-1)

from __future__ import print_function
import argparse
import lib

def cmd_parser():
    """
    The commandline parser logic
    """

    description = "A tool to help discover the terminal commands on your Unix Based Machine."
    epilog = "use: 'man [cmd]' or '[cmd] -h' to see how that cmd is used"

    # Initilize the arg parser
    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    group1 = parser.add_mutually_exclusive_group(required=True)
    group1.add_argument("-d, --default",
          help="lists files from /usr/bin directory",
          action="store_true")
    group1.add_argument("-l, --local",
          help="lists files from the /usr/local/bin directory",
          action="store_true")
    group1.add_argument("-a, --all",
          help="Lists files from both /usr/bin and /usr/local/bin directories",
          action="store_true")

    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument("-s, --startswith",
          help="applies a grep '^char' filter to the output",
          type=str)
    group2.add_argument("-i, --includes",
          help="applies a grep 'string' filter to the output",
          type=str)

    args = vars(parser.parse_args())
    return args

if __name__ == '__main__':
    args = cmd_parser()
    print(lib.format_args(args))

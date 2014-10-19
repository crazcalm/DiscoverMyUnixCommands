DiscoverMyUnixCommands
======================

Back Story:
-----------
      I was reading "Python: for Unix and Linux System Administration" when I
    came accross the default location for most of my computer's terminal
    commands. While looking through the list, I realized that I only knew
    of the more common commands, but there a plenty of other useful commands
    on my computer.

      I am writing this tool in hope that I can use it to become more familiar
    with these commands.

Description:
------------
    A tool to help discover the terminal commands on your Unix Based Machine.

Install:
--------
    git clone git@github.com:crazcalm/DiscoverMyUnixCommands.git

Usage:
------
    input: python unix_cmd.py -h

    output: usage: unix_cmd.py [-h] (-d, --default | -l, --local | -a, --all)
                   [-s, --startswith S, __STARTSWITH | -i, --includes I, __INCLUDES]

            A tool to help discover the terminal commands on your Unix Based Machine.

            optional arguments:
              -h, --help            show this help message and exit
              -d, --default         lists files from /usr/bin directory
              -l, --local           lists files from the /usr/local/bin directory
              -a, --all             Lists files from both /usr/bin and /usr/local/bin
                                    directories
              -s, --startswith S, __STARTSWITH
                                    applies a grep '^char' filter to the output
              -i, --includes I, __INCLUDES
                                    applies a grep 'string' filter to the output

            use: 'man [cmd]' or '[cmd] -h' to see how that cmd is used

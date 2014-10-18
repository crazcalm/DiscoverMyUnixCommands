#!/usr/bin/python
import subprocess

def ls_dir_grep(dirs, grep_arg):
    """
    Pipes an ls command into grep
    """
    command = 'ls %s | grep "%s"' %(dirs, grep_arg)
    subprocess.call([command], shell= True)

def ls_dir(dirs):
    """
    ls command on directories
    """
    command = 'ls %s' % dirs
    subprocess.call([command], shell=True)


if __name__ == '__main__':
    #ls_dir_grep("/usr/bin", "a")
    ls_dir("/usr/bin /usr/local/bin")
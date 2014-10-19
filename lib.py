from __future__ import print_function
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

def format_args(args):
    """
    Formats the command line args program
    """
    settings = {
        "grep": False,
        "dirs": "",
        "grep_include":"",
        "grep_startswith":"",
    }

    for key,value in args.iteritems():
        if key.startswith("s") and value != None:
            settings["grep"] = True
            settings["grep_startswith"] = value[0]

        elif key.startswith("i") and value !=None:
            settings["grep"] = True
            settings["grep_include"] = value

        if key.startswith("d") and value:
            settings["dirs"] = "/usr/bin"

        elif key.startswith("l") and value:
            settings["dirs"] = "/usr/local/bin"

        elif key.startswith("a") and value:
            settings["dirs"] = "/usr/bin /usr/local/bin"

    return settings




if __name__ == '__main__':
    #ls_dir_grep("/usr/bin", "a")
    #ls_dir("/usr/bin /usr/local/bin")
    test = {"a":True, "d":False, "l":False, "s":None, "i":"hello"}
    format_args(test)
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

def run_commands(settings):
    """
    Checks the settings and runs the needed commands
    """
    dirs = settings["dirs"]

    if settings["grep"]:
        if settings["grep_startswith"] != "":
            grep = settings["grep_startswith"]
        else:
            grep = settings["grep_include"]

        ls_dir_grep(dirs, grep)

    else:
      ls_dir(dirs)


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

    try: #python 2
        for key,value in args.iteritems():
            if key.startswith("s") and value != None:
                settings["grep"] = True
                settings["grep_startswith"] = "^" + value

            elif key.startswith("i") and value !=None:
                settings["grep"] = True
                settings["grep_include"] = value

            if key.startswith("d") and value:
                settings["dirs"] = "/usr/bin"

            elif key.startswith("l") and value:
                settings["dirs"] = "/usr/local/bin"

            elif key.startswith("a") and value:
                settings["dirs"] = "/usr/bin /usr/local/bin"

    except AttributeError: #python 3.4
        for key,value in args.items():
            if key.startswith("s") and value != None:
                settings["grep"] = True
                settings["grep_startswith"] = "^" + value

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
    ls_dir_grep("/usr/bin", "^a")
    ls_dir("/usr/bin /usr/local/bin")
    test = {"a":True, "d":False, "l":False, "s":None, "i":"hello"}
    format_args(test)
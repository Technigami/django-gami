from fabric.api import *
from fabric.colors import yellow, green, blue, red


###########################################
# Utils and wrappers for various commands #
###########################################

# from Mezzanine::

def _print(output):
    print
    print output
    print


def print_command(command):
    _print(blue("$ ", bold=True) +
           yellow(command, bold=True) +
           red(" ->", bold=True))

@task
def clone(repo, show=True):
    """
    Clones 
    """
    repo_str = ""
    response = ""
    if repo.endswith(".git"):
        repo_str = "git clone git@technigami.com:"+repo
    else:
        repo_str = "git clone git@technigami.com:"+repo+".git"
 
    try:
        local(repo_str)
        _print(green("Successfully cloned "+ repo, bold=True))
    except:
        _print(red("Could not clone repository.  Either it didn't exist or you don't have access.  email dan@technigami.com with the name of the repository you're trying to clone.",bold=True))    

@task
def workon(repo, show=True):
    """
    Gets everything set up to work on a new technigami project,
    or gets your environment switched to a project repo if it exists.
    """
    
    reponame = repo.replace(".git","")
    try:
        local("workon " + reponame)
    except:
        local("mkvirtualenv "+reponame)
    

    try:
        with open("~/technigami/"+reponame): pass
    except IOError:
        print Fore.ORANGE + "Repository " + reponame + " didn't exist.  Attempting to clone"
        print Fore.RESET
        
        with cd("~/technigami/"):
            clone(repo)

def ls():
    """
    Test command
    """
    local('ls')

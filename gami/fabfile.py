from fabric.api import *
from colorama import Fore, Back, Style

def clone(repo):
    repo_str = ""
    response = ""
    if repo.endswith(".git"):
        repo_str = "git clone git@technigami.com:"+repo
    else:
        repo_str = "git clone git@technigami.com:"+repo+".git"
 
    try:
        local(repo_str)
        print ""
        print Fore.GREEN + "Successfully cloned "+repo
        print Fore.RESET
    except:
        print ""
        print Fore.RED + "Could not clone repository.  Either it didn't exist or you don't have access.  email dan@technigami.com with the name of the repository you're trying to clone."
        print Fore.RESET
    

def workon(repo):
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
    run("ls")

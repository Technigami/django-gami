from fabric.api import *
from fabric.colors import yellow, green, blue, red


###########################################
# Utils and wrappers for various commands #
###########################################
# Config (move to another file)
gitolite_admin = "/Users/dag/business/gitolite-admin"
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
def init(name = None, show=True):
    """
    Initialize a new project
    
    - Set up a new virtualenv
    - Enable it
    - Set up a new git repository
    - Set up a registration job
    
    """
    # takes the name of the repository or none for interactive shell
    # assumes you're in the directory you want to initialize the project in
    
    # Check to see if the git repository already exists
    if 
    
    if name == None:
        name = os.getcwd().split('/')[-1]
    
    gitolite_config = gitolite_admin+'/conf/gitolite.conf'
    
    local('git init .')
    local('git add .')
    local('git commit -am "initial commit"')
    local('git remote add origin git@technigami.com:'+name+".git")

    local('echo "repo       '+name+'\n       RW+ = @staff" >> '+ gitolite_config)
    
    with lcd(gitolite_admin):
        local('git commit -am "adding new repository"; git push')
        local('git push origin master')

    local('git push origin master')


@task
def server():
    """
    Not yet implemented.  This launches a local webserver
    Allows you to inspect your local install of your django code.
    """
    pass

@task
def deploy():
    """
    deploys to servers defined in your config file.
    """
    pass
    
@task
def register():
    """
    Submits your keys to the technigami server.
    """
    pass


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



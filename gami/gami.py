from fabric.tasks import execute
from fabfile import clone,workon
import sys

def command_switcher(arguments):
    if len(arguments) < 2:
        print "Call gami [command]"
        return -1

    elif arguments[1] == 'clone' and len(arguments) == 3:
        clone(arguments[2])
    elif arguments[1] == 'workon' and len(arguments) == 3:
        workon(arguments[2])

if __name__ == "__main__":
    # Parse command line arguments for gami
    command_switcher(sys.argv)

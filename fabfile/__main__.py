"""proc

Usage:
  proc install [--debug|--local] <environnement>
  proc update [--debug|--local] <environnement>
  proc (-h | --help)
  proc --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --debug       Only print the command to the prompt.
  --local       Run the command in the local environnement.

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Procedure beta 0.0.1')
    print(arguments)

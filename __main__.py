"""proc

Usage:
  proc install [-rd] <environnement>
  proc update [-rd] <environnement>
  proc jenkins_install [-d] <password>
  proc jenkins_update [-d]
  proc (-h | --help)
  proc --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  -r, --remote  execute the command on remote server
  -d, --debug   Only print the command to the prompt.

"""
from docopt import docopt
from fabfile import *

if __name__ == '__main__':
  arguments = docopt(__doc__, version='Procedure beta 0.0.1')
  if(arguments['--debug']):
    print(arguments)
  if(arguments['--remote']):
    remote(arguments['<environnement>'])
  elif(arguments['jenkins_install'] or arguments['jenkins_update'] ):
    jenkins()
  else:
    local(arguments['<environnement>'])


  #debug needs to be excute after the local(), jenkins or  remote()
  if(arguments['--debug']):
    debug()

  if(arguments['install']):
    install()

  if(arguments['jenkins_install']):
    jenkins_install_build(arguments['<password>'])

  if(arguments['update'] or arguments['jenkins_update']):
    update_project()



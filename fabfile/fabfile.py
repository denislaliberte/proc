from fabric.api import *
from fabric.operations import local as lrun, run
from fabric.utils import puts
from StupidConfig import *
import string
from drush import *
from fabric.contrib.console import confirm
jenkins_workspace = "/var/lib/jenkins/workspace/project"

## use this stask to debug fab commad
## exemple fab fabfile.local fabfile.debug fabfile.task
## dont execute the command, only print to console
@task 
def debug():
  env.run = puts

@task 
def local(configfile = ""):
  set_environnement(configfile)
  env.run = lrun

def set_environnement(configfile):
  global env_url
  if not configfile:
    configfile = raw_input("Enter the configuration file name 'example local.com' :")
  global config
  config = generate_config(configfile)
  host = config.get_variable("hostname")
  env.hosts = [host]

@task 
def remote(configfile = ""):
  set_environnement(configfile)
  env.ssh = config.get_variable("ssh")
  env.run = run

@task
def jenkins():
  env.run = lrun
  global config
  env.run("export PATH=$PATH:/usr/bin")
  procedure_path = jenkins_workspace + "/sites/procedures"
  config = generate_config_absolute_path("file_to_commit/jenkins",procedure_path)
  env.hosts = ['localhost']
  configure_behat(config)

## task  ##
@task 
def jenkins_install_build(db_password):
  config.set_variable('db_password',db_password)
  instal(True)
  project_path = config.get_variable("project_path")
  command_composer = project_path +"/sites/tests/bin/composer.phar install --working-dir="+project_path +"/sites/tests"
  env.run(command_composer)

@task
def instal(no_prompt=False):
  install_command = install_drupal(config, no_prompt)
  deploy_module = config.get_variable("deploy_module")
  install_module_command = install_module(deploy_module,config)
  clear_cache_command = create_drush_command(config,"cache-clear all")
  revert_feature = create_drush_command(config,"features-revert-all -y")
  l10n_update = create_drush_command(config,"l10n-update")
  try:
   env.run(install_command)
   env.run(install_module_command)
   env.run(clear_cache_command)
   env.run(revert_feature)
   env.run(l10n_update)
  finally:
    if not no_prompt:
      write_variables()

def write_variables():
  if config.new_value_to_write():
    print "Procedures variables :"
    print config.get_config_variable()
    if confirm("Write variables in the config_file/*yaml ?"):
      config.dump_to_file()


def configure_behat(config):
  behat_config_path = config.get_variable("project_path") + "/sites/tests/behat.yml"
  behat_config = StupidConfig(behat_config_path)
  default = behat_config.get_variable("default")
  url = "http://" + config.get_variable("local_url")
  default['extensions']['Behat\MinkExtension\Extension']['base_url']=url
  default['extensions']['Drupal\DrupalExtension\Extension']['drush']['root']=config.get_variable("project_path")
  behat_config.set_variable('default',default)
  behat_config.dump_to_file()

@task
def update_project():
  update_command = create_drush_command(config,"updatedb")
  clear_cache = create_drush_command(config,"cache-clear all")
  env.run(update_command)
  env.run(clear_cache)

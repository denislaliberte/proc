
def install_drupal(config,no_prompt):
  installation_command = get_install_drupal_command(config)
  installation_command_parameters = get_install_drupal_parameters(config)
  if no_prompt:
    install_arg = " -y"
  else:
    install_arg = ""
  command = installation_command + install_arg +installation_command_parameters
  drush_command = add_drush_path(command,config)
  return drush_command

def get_install_drupal_command(config):
  command_placeholder = "site-install standard --db-url=mysql://{db_user}:{db_pass}@{url}/{name}"
  db_name = config.get_variable('db_name')
  db_user = config.get_variable('db_user')
  db_password = config.get_variable('db_password')
  db_url = config.get_variable('db_url')
  command = command_placeholder.format(db_user=db_user,db_pass=db_password,url=db_url,name=db_name)
  return command 

def get_install_drupal_parameters(config):
  parameter_placeholder =  " --account-name={drupal_name} --account-pass={drupal_pass} --site-name={site_name}"
  drupal_user_name = config.get_variable('drupal_user_name')
  drupal_user_password = config.get_variable("drupal_user_password")
  site_name = config.get_variable('site_name')
  parameter =parameter_placeholder.format(drupal_name=drupal_user_name,drupal_pass=drupal_user_password,site_name=site_name)
  return parameter

def add_drush_path(command_argument,config):
  command_placeholder = "drush -r {path} " +command_argument
  project_path = config.get_variable('project_path')
  command = command_placeholder.format(path=project_path)
  return command

def install_module(module_name,config):
  command_placeholder = "pm-enable -y {module}"
  command = command_placeholder.format(module=module_name)
  drush_command = add_drush_path(command,config)
  return drush_command

def create_drush_command(config,command):
  drush_command = add_drush_path(command,config)
  return drush_command


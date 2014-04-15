fabric library to handle drupal project CI and deployment
=========================================================

## Warning ##
The script will write your password to the configfile/myconfig.yaml
See the .gitignore

## exemple ##
### debug the command ###
Test the output of your script before execute them
fab fabfile.local fabfile.debug fabfile.instal

### environnement ###
chose your environnement 
fab fabfile.local @task
fab fabfile.jenkins @task
fab fabfile.remote @task


### task ###
fab @environnement fabfile.instal
fab @environnement fabfile.generate_content
fab @environnement fabfile.update_project

### jenkins ###
jenkins run the command locally without prompt you can add them to a shell build
step

fab fabfile.jenkins fabfile.jenkins_install_build:db_password=my_password
fab fabfile.jenkins fabfile.update_project




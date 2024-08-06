pipeline {
    agent any
    
    stages {
        stage('git') {
            steps {
                git 'https://github.com/Ajayjohn96/project1.git'
            }
        }
        stage('pip and venv') {
            
            steps {
                sh '''
                #!/bin/bash
                apt-get install python3-pip python3-venv -y
                '''
            }
        }
        stage('virtual environment creation') {
            steps {
                sh '''#!/bin/bash
                    python3 -m venv my_env
                    source my_env/bin/activate
                    '''
            }
        }
        stage('django installation') {
            steps {
                sh '''#!/bin/bash
                source my_env/bin/activate
                pip install django'''
            }
        }
        stage('test') {
            steps {
                sh '''#!/bin/bash
                source my_env/bin/activate
                python3 manage.py test'''
            }
        }
        stage('migrate') {
            steps {
                sh '''#!/bin/bash
                source my_env/bin/activate
                python3 manage.py migrate'''
            }
        }
        stage('SonarQube Analysis') {
          steps{
             def scannerHome = tool 'sonarqube-scanner';
             withSonarQubeEnv() {
             sh "${scannerHome}/bin/sonar-scanner"
              }
          }
      }
    }
}


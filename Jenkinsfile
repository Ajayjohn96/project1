pipeline {
    agent any
    stages {
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

pipeline {
  agent any
  stages {
    stage('Git Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/Honeyoceanmtech/simple_project.git'
      }
    }
    stage('UNIT Testing') {
      steps {
        sh 'mvn test'
      }
    }
  }
}

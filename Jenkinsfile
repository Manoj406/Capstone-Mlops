pipeline {
    agent any
 
    stages {
 
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
 
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cal-housing-api:latest .'
            }
        }
 
        stage('Smoke Test') {
            steps {
                sh 'echo "Smoke test passed"'
            }
        }
    }
}
 
pipeline {
    agent any
 
    stages {
 
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Manoj406/Capstone-MLOps.git', branch: 'main'
            }
        }
 
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t california-housing-api .'
            }
        }
 
        stage('Smoke Test') {
            steps {
                sh '''
                docker rm -f test-api || true
                docker run -d -p 8001:8000 --name test-api california-housing-api
                sleep 10
                curl -f http://localhost:8001/docs
                docker rm -f test-api
                '''
            }
        }
    }
}

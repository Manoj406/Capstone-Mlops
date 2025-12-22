pipeline {
    agent any
 
    stages {
 
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Manoj406/Capstone-MLOps.git'
            }
        }
 
        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t california-housing-api .
                '''
            }
        }
 
        stage('Test Container') {
            steps {
                sh '''
                docker run -d -p 8001:8000 --name test-api california-housing-api
                sleep 10
                curl http://localhost:8001/docs
                docker rm -f test-api
                '''
            }
        }
    }
}pipeline {
    agent any
 
    stages {
 
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Manoj406/Capstone-MLOps.git'
            }
        }
 
        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t california-housing-api .
                '''
            }
        }
 
        stage('Test Container') {
            steps {
                sh '''
                docker run -d -p 8001:8000 --name test-api california-housing-api
                sleep 10
                curl http://localhost:8001/docs
                docker rm -f test-api
                '''
            }
        }
    }
}

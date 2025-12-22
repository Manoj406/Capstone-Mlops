pipeline {
    agent any
 
    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out successfully'
            }
        }
 
        stage('Sanity Check') {
            steps {
                sh 'echo "Jenkins pipeline is working"'
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/jabedzaman/devops.git'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose build'
                sh 'docker-compose up -d'
            }
        }
    }
}

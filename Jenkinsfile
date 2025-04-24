pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'jabedzaman/devops-api' 
        DOCKER_TAG = 'latest' 
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/jabedzaman/devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} -f app/Dockerfile ./app'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'd9cf6508-25f8-4539-9e8f-bcb1c3168e0f', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker compose down
                    docker compose pull
                    docker compose up -d
                '''
            }
        }
    }
}

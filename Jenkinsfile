pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage("Clone repository") {
            steps {
                git branch: 'main',
                    url: 'https://github.com/michaelbenis/Cyber-incident.git'
            }
        }
        stage("Build image") {
            steps {
                script {
                    def repo = "https://github.com/michaelbenis/Cyber-incident.git"
                    def branch = "main"
                }
                sh 'docker build --build-arg REPO_TO_CLONE=$repo --build-arg BRANCH_TO_MERGE=$branch -t merge-image .'
            }
        }
        stage("Run container") {
            steps {
                sh 'docker run merge-image'
            }
        }
    }
}

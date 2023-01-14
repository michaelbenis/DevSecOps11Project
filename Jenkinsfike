pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage("Build image") {
            steps {
                script {
                    def repo = "$REPO_TO_CLONE"
                    def branch = "$BRANCH_TO_MERGE"
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
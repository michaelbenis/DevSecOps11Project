pipeline {
    agent any
    stages {
        stage("Clone repository") {
            steps {
                git branch: env.BRANCH_TO_MERGE,
                    url: env.REPO_TO_CLONE
            }
        }
        stage("Build image") {
            steps {
                sh 'docker build --build-arg REPO_TO_CLONE=$REPO_TO_CLONE --build-arg BRANCH_TO_MERGE=$BRANCH_TO_MERGE -t merge-image .'
            }
        }
        stage("Run container") {
            steps {
                sh 'docker run merge-image'
            }
        }
    }
}

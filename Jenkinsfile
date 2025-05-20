pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'baa7016a-1c21-47f5-a3a9-97efe7fc1a8c', url: 'https://github.com/darshiljani/jenkins-site-tutorial'
            }
        }
        stage('Setup Python Environment') {
            steps {
                dir('backend') {
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install -r requirements/prod.txt'
                }
            }
        }
        stage('Backend Linting & Formatting Check') {
            steps {
                dir('backend/server') {
                    script {
                        sh './venv/bin/ruff check . --fix --exclude "templates"'
                        sh './venv/bin/ruff format . --diff --exclude "templates"'
                    }
                }
            }
        }
        stage('Backend Unit Tests') {
            steps {
                dir('backend/server') {
                    sh 'python manage.py test'
                }
            }
        }
        stage('Frontend Type Checking') {
            steps {
                dir('frontend') {
                    script {
                        def typeCheckResult = sh(script: 'tsc --noEmit', returnStatus: true)
                        if (typeCheckResult != 0) {
                            error('Frontend type checking failed! Cancelling commit.')
                        }
                    }
                }
            }
        }
        stage('Frontend Linting & Formatting Check') {
            steps {
                dir('frontend') {
                    script {
                        sh 'npm run lint'
                        sh 'npm run format'
                        echo 'Frontend linting & formatting completed!'
                    }
                }
            }
        }
        stage('Frontend Unit Tests') {
            steps {
                dir('frontend') {
                    script {
                        def testResult = sh(script: 'npm run test', returnStatus: true)
                        if (testResult != 0) {
                            error('Frontend unit tests failed! Cancelling commit.')
                        }
                    }
                }
            }
        }
        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'npm run build'
                    echo 'Frontend built successfully!'
                }
            }
        }
    }
    post {
        success {
            echo 'All checks passed!'
        }
        failure {
            error('Tests or type checks failed! Cancelling build.')
        }
    }
}
pipeline {
    agent any

    tools {
        nodejs 'NodeJS'
    }
    
    environment {
        DJANGO_SECRET_KEY = credentials('site_secret_key')
        APP_ENV = "prod"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/darshiljani/jenkins-site-tutorial'
            }
        }
        stage('Setup Python Environment') {
            steps {
                dir('backend') {
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install -r requirements/prod.txt'
                    sh 'echo $DJANGO_SECRET_KEY > ./server/.secret_key'
                }
            }
        }
        stage('Backend Linting & Formatting Check') {
            steps {
                dir('backend') {
                    script {
                        sh './venv/bin/ruff check ./server/ --select I --fix --exclude "templates"'
                        sh './venv/bin/ruff format ./server/ --exclude "templates" > /dev/null'
                    }
                }
            }
        }
        stage('Backend Unit Tests') {
            steps {
                dir('backend') {
                    sh './venv/bin/python3 server/manage.py test'
                }
            }
        }
        stage('Setup Frontend Environment') {
            steps {
                dir('frontend') {
                    sh 'npm ci'
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
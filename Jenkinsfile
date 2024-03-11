pipeline {
    agent any

    enviorment{
        env_variable = 'value'
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git 'https://github.com/zeeshanali10771/mlops-class-activity-2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                script {
                    bat 'pip3 install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run test.py using pytest
                script {
                    bat 'pytest test.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Get the branch name
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()

                    // Deploy based on the branch name
                    if (branchName == 'main') {
                        echo 'Deploying to production'
                        // Add production deployment steps here
                    } else {
                        echo 'Deploying to UAT'
                        // Add UAT deployment steps here
                    }
                }
            }
        }
    }
}

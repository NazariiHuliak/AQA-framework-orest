pipeline {
    agent any

    environment {
        PYTHONPATH = "%WORKSPACE%"
    }

    stages {

        stage('Setup Python') {
            steps {
                bat """
                python --version
                pip install --upgrade pip
                """
            }
        }

        stage('Install Python dependencies') {
            steps {
                bat """
                if exist requirements.txt (
                    pip install -r requirements.txt
                )
                """
            }
        }

        stage('Run tests') {
            steps {
                bat """
                set PYTHONPATH=%PYTHONPATH%;%WORKSPACE%
                python -m pytest tests/run_all_tests.py
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/test-reports/*.xml', allowEmptyArchive: true
        }
        failure {
            echo "Tests failed!"
        }
    }
}

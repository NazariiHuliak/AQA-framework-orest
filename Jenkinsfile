pipeline {
    agent any

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
    }

    agent {
        docker {
            image 'python:3.11'
            args '-u root'
        }
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh """
                    apt-get update
                    apt-get install -y wget gnupg unzip \
                    xvfb libnss3 libxss1 libatk1.0-0 \
                    libcups2 libdrm2 libxcomposite1 libxrandr2 \
                    libgbm1 libpango-1.0-0 libpangocairo-1.0-0 \
                    libasound2t64 libatspi2.0-0 libgtk-3-0

                    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
                    dpkg -i google-chrome-stable_current_amd64.deb || apt --fix-broken install -y

                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run tests') {
            steps {
                sh """
                    pytest tests/run_all_tests.py
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

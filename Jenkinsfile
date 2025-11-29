pipeline {
    agent any

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/username/repo.git', branch: 'test'
            }
        }

        stage('Set up Python & Dependencies') {
            steps {
                script {
                    sh '''
                        python3 --version || sudo apt-get update && sudo apt-get install -y python3.11 python3.11-venv python3.11-dev python3-pip
                        python3 -m pip install --upgrade pip
                    '''

                    sh '''
                        sudo apt-get install -y wget gnupg unzip xvfb libnss3 libxss1 libatk1.0-0 \
                        libcups2 libdrm2 libxcomposite1 libxrandr2 libgbm1 libpango-1.0-0 \
                        libpangocairo-1.0-0 libasound2 libatspi2.0-0 libgtk-3-0

                        wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
                        sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt --fix-broken install -y
                    '''

                    sh '''
                        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                    python -m pytest tests/run_all_tests.py
                '''
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

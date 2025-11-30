pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\Orik\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    }

    stages {

        stage('Install dependencies') {
            steps {
                bat """
                    "%PYTHON_PATH%" -m pip install --upgrade pip
                    if exist requirements.txt "%PYTHON_PATH%" -m pip install -r requirements.txt
                """
            }
        }

        stage('Run tests') {
            steps {
                bat """
                    "%PYTHON_PATH%" -m pytest tests\\run_all_tests.py --junitxml=test-reports\\results.xml
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**\\test-reports\\*.xml', allowEmptyArchive: true
        }
        failure {
            echo "Tests failed!"
        }
    }
}

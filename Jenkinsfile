pipeline {
    agent any

    stages {

        stage('Install dependencies') {
            steps {
                bat """
                    python -m pip install --upgrade pip
                    if exist requirements.txt python -m pip install -r requirements.txt
                """
            }
        }

        stage('Run tests') {
            steps {
                bat """
                    python -m pytest tests\\run_all_tests.py --junitxml=test-reports\\results.xml
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

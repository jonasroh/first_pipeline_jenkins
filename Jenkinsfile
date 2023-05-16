/* Requires the Docker Pipeline plugin */
pipeline {
    agent any 
    stages {
        stage('Clonar repositório') {
            steps {
                git 'https://github.com/jonasroh/first_pipeline_jenkins.git'
            }
        }

        stage('Construir ambiente') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage ('Implantar aplicação'){
            steps {
                sh 'python app.py &'
            }
        }
    }
}
